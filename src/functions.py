import pickle
import re
import pandas as pd
import unidecode


##### Demonym Dictionary Notebook #####
region_replacement_dictionary = {    
    'Ciudad de Mexico': 'Mexico City',
    'Coahuila de Zaragoza': 'Coahuila',
    'Michoacan de Ocampo': 'Michoacan',
    'State of Mexico': 'Mexico'
}

def change_df_names(dataframe, region_col):
    df_col_list = list(dataframe.columns)
    region_col_index = df_col_list.index(region_col)
    if region_col_index == 0:
        dataframe.columns = ['region', 'name']
    elif region_col_index == 1:
        dataframe.columns = ['name', 'region']
    # also cleaning the names of regions within the notebook
    dataframe['region'] = [unidecode.unidecode(x) for x in dataframe['region']]
    return dataframe
        
def match_region_names(dictionary, dataframe):
    actual_regions = list(dictionary.keys())
    dataframe_columns = list(dataframe['region'].unique())
    non_matched_col_names = []
    for item in dataframe_columns:
        if item not in actual_regions:
            non_matched_col_names.append(item)
    return non_matched_col_names

def replace_col_values_in_df(dataframe,  repl_dict = region_replacement_dictionary):
    dataframe['region'].replace(repl_dict, inplace=True)
    return dataframe

def add_data_to_dictionary(dataframe, dictionary):
    # cycle thru the dataframe, adding each entry (also if list)
    ## determining if the dataframe has each entry in a list
    type_of_entries = type(dataframe['name'].iloc[0])
    if type_of_entries == list:
        for idx in range(len(dataframe)):
            region = dataframe.region.iloc[idx]
            dictionary[region].extend(dataframe.name.iloc[idx])
    elif type_of_entries == str:
        for idx in range(len(dataframe)):
            dictionary[dataframe.region.iloc[idx]].append(dataframe.name.iloc[idx])
    return dictionary

def clean_dictionary_values(dictionary):
    mexico_regional_names_dict_lower = {}
    for key, value in dictionary.items():
        mexico_regional_names_dict_lower[key] = []
        for y in value:
            # I had an issue that the last item of each key was a sequence of lists
            if type(y) == str:
                lower_y = y.lower()
                no_accent_lower_y = unidecode.unidecode(lower_y)
                if no_accent_lower_y not in mexico_regional_names_dict_lower[key]:
                    mexico_regional_names_dict_lower[key].append(no_accent_lower_y)
    # removing values that are keys to a different entry
    for key in mexico_regional_names_dict_lower.keys():
        lower_key = key.lower()
        temp_keys = list(mexico_regional_names_dict_lower.keys())
        temp_keys.remove(key)
        for item in temp_keys:
            if key in mexico_regional_names_dict_lower[item]:
                mexico_regional_names_dict_lower[item].remove(key)
            if lower_key in mexico_regional_names_dict_lower[item]:
                mexico_regional_names_dict_lower[item].remove(lower_key)
    return mexico_regional_names_dict_lower
     
##### Matching Cities to Mexican Restaurants #####
def find_matches(restaurant_list, dictionary):
    match_list = []
    for rest in restaurant_list:
        split_rest_name = rest.split()
        for word in split_rest_name:
            for key, value in dictionary.items():
                final_list = list(set([word]) & set(value))
                if len(final_list) >= 1:
                    match_list.append(rest)
                    pass
    return match_list

def find_regions_for_restaurants(rest_list, dictionary):
    unique_rest_matches = list(set(rest_list))
    rest_matches_w_regions = {x: {None:[]} for x in unique_rest_matches}
    for key, value in rest_matches_w_regions.items():
        split_item = key.split()
        for word in split_item:
            for key1, value1 in dictionary.items():
                for city in value1:
                    if word == city:
                        if rest_matches_w_regions[key].get(word):
                            if [key1, city] not in rest_matches_w_regions[key][word]:
                                rest_matches_w_regions[key][word].append([key1, city])
                        else:
                            rest_matches_w_regions[key] = {word: [[key1, city]]}
    return rest_matches_w_regions
       
# adding city, restaurants, and region matches to a single dataframe
city_df_columns = ['Restaurant', 'City', 'Matched_word', 'Region', 'Multiple_regions_flag', "Final_region"]
# all_cities_df = pd.DataFrame(columns = city_df_columns)
def add_city_to_all_cities_dict(rest_matches_w_regions, city_name, df_cols=city_df_columns):
    matched_words_list = [x for item in rest_matches_w_regions.values() for x in item]
    all_matched_regions = []
    for key, value in rest_matches_w_regions.items():
        for key1, value1 in value.items():
            region_str = ""
            regions_list = []
            for sublist in value1:
                region_str += sublist[0] + ","
            all_matched_regions.append(region_str[0:-1])
    matched_region_flag = [False if x.count(",") > 0 else True for x in all_matched_regions]
#     city_df = pd.DataFrame(data = [[list(rest_matches_w_regions.keys()), 
#                                    "", 
#                                    matched_words_list,
#                                    all_matched_regions,
#                                    matched_region_flag,
#                                    ""]],
#                            columns = df_cols
#     )
#     final_df = input_df.append(city_df, ignore_index = True)
#     final_df
#     final_df['City'] = city_name
    input_df = pd.DataFrame(columns = df_cols)
    input_df['Restaurant'] = list(rest_matches_w_regions.keys())
    input_df['City'] = city_name
    input_df['Matched_word'] = matched_words_list
    input_df['Region'] = all_matched_regions
    input_df['Multiple_regions_flag'] = matched_region_flag
    input_df['Final_region'] = ""
    return input_df
    