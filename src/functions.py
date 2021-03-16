import pickle
import re
import pandas as pd
import unidecode
import random
from collections import OrderedDict


##### Demonym Dictionary Notebook #####
region_replacement_dictionary = {    
    'Ciudad de Mexico': 'Mexico City',
    'Coahuila de Zaragoza': 'Coahuila',
    'Michoacan de Ocampo': 'Michoacan',
    'State of Mexico': 'Mexico',
    'Distrito Federal': "Mexico City",
    'Estado de Mexico': "Mexico"
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
    input_df = pd.DataFrame(columns = df_cols)
    input_df['Restaurant'] = list(rest_matches_w_regions.keys())
    input_df['City'] = city_name
    input_df['Matched_word'] = matched_words_list
    input_df['Region'] = all_matched_regions
    input_df['Multiple_regions_flag'] = matched_region_flag
    input_df['Final_region'] = ""
    return input_df
    
##### Analysis Notebook #####
def count_regions_in_city(city, df):
    city_regions = {}
    city_df = df[df['City'] == city]
    for idx, x in enumerate(city_df.Final_region):
        if x in city_regions:
            city_regions[x] += 1
        else:
            city_regions[x] = 1
    return city_regions

def add_regions_for_city_regions_count(city_regions, all_regions):
    for x in all_regions:
        if x not in city_regions:
            city_regions[x] = 0
    sorted_region_values = [city_regions[key] for key in sorted(city_regions)]
    return sorted_region_values

# according to https://www.picos.net/the-seven-regions-of-mexican-cuisine/
cul_reg_dict = {"North": ['Baja California', "Baja California Sur",
                         "Sonora", "Chihuahua", "Coahuila", "Durango",
                         'Zacatecas', "Aguascalientes", "Nuevo Leon", 
                          'Tamaulipas'],
                "North Pacific Coast": ['Sinaloa', 'Nayarit', 'Jalisco',
                                       'Colima'],
                "Bajio": ['Michoacan', "Michoacan de Ocampo", 
                          'Guanajuato', 'San Luis Potosi', 'Queretaro'],
                "South Pacific Coast": ['Guerrero', 'Oaxaca', 'Chiapas'],
                "South": ['Campeche', "Yucatan", "Quintana Roo"],
                "Gulf": ['Tabasco', 'Veracruz'],
                "Central": ['Mexico', 'Puebla', 'Morelos', 'Tlaxcala', "Hidalgo", "Mexico City",
                           'Ciudad de Mexico', "Distrito Federal", 'Ciudad De Mexico']
                }
def turn_city_regions_to_cul_regions(city_regions, cul_regions=cul_reg_dict):
    city_cul_regions = {key:0 for key in cul_regions.keys()}
    for key, value in city_regions.items():
        for key2, value2 in cul_regions.items():
            if key.title() in value2:
                city_cul_regions[key2] += value
    return city_cul_regions

def turn_regions_to_cul_regions(cul_reg_dict=cul_reg_dict):
    region_to_cul_reg_dict = {}
    for key, value in cul_reg_dict.items():
        for item in value:
            region_to_cul_reg_dict[item] = key
    return region_to_cul_reg_dict

def select_random_restaurants(city, df):
    # input restaurants_df (full, original df)
    new_df = df[df['City'] == city].reset_index(drop=True)
    new_indices = []
#     region_dict = {key:0 for key in all_regions}
# pick 10 random numbers and use those indices
    random_nums = []
    while len(random_nums) < 10:
        random_number = random.randint(0, len(new_df)-1)
        if random_number not in random_nums:
            random_nums.append(random_number)
    final_df = new_df[new_df.index.isin(random_nums) == True]
    return final_df

def interpret_random_restaurants_df(df):
    # rest_df
    count_of_regions = df.Final_region.nunique()
    count_of_culinary_regions = df.Culinary_region.nunique()
    return count_of_regions, count_of_culinary_regions

def get_5_samples_of_rand_regions(city, df):
    df_list = []
    region_counter = 0
    culinary_region_counter = 0
    while len(df_list) < 5:
        df_trial = select_random_restaurants(city, df)
        region_count, culinary_region_count = interpret_random_restaurants_df(df_trial)
        region_counter += region_count
        culinary_region_counter += culinary_region_count
        df_list.append(df_trial)
    mean_region_count = round(region_counter / 5, 1)
    mean_culinary_region_count = round(culinary_region_counter / 5, 1)
    print(f"For {city} the mean number of regions is {mean_region_count} and the mean number of culinary_regions is {mean_culinary_region_count}")
    return mean_region_count, mean_culinary_region_count

def find_region_counts_list(city_name, df, demonym_dict, gdf):
    rest_count_dict = {key:0 for key in demonym_dict.keys()}
    city_df = df[df['City'] == city_name].reset_index()
    for idx in range(len(city_df['City'])):
        region = city_df['Final_region'][idx]
        if region in rest_count_dict.keys():
            rest_count_dict[region] += 1
        else:
            rest_count_dict[region] = 0
    rest_count_dict_sorted = OrderedDict(sorted(rest_count_dict.items(), key=lambda t: t[0]))
    rest_counts = list(rest_count_dict_sorted.values())
    city_name_count = city_name + "_count"
    gdf[city_name_count] = rest_counts
    return gdf