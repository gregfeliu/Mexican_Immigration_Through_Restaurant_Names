# Mexican Immigration Through Restaurant Names

## Description
Mexican immigration to the United States has a long and interesting history. There are 4 major periods to this migration that have led to the distribution of people of Mexican descent to where they live today. In this project, **I aim to discover more about the distribution of Mexicans in 4 major cities with a significant Mexican-heritage population: New York City, Chicago, Dallas and San Francisco**. 

### Historical Background
Mexican Immigration to the United States is [generally characterized](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146) by _pull_ factors to the United States with certain periods of Mexican history creating _push_ factors for migration with the constant theme of poverty pushing them northward. Traditionally, Mexican men worked in agriculture in the American Southwest and waited until the next harvest either by returning to Mexico or temporarily living in nearby U.S. cities. It wasn't until the Great Depression where anti-immigrant sentiment started making this porous U.S.-Mexico border into a firm one. This theme continued until the relatively firm border that we have today. Starting in World War 2, Mexican labor was needed to fill the gaps in rural labor left by the war. Thereafter, Mexican labor began diversifying and moving beyond the American Southwest. This was even more so after the Immigration Control and Reform Act of 1986 (IRCA). This law aimed to end illegal immigration by granting citizenship to all Mexican immigrants who arrived pre-1982. This led to this already in the U.S. to [bring their families and seek out a life in the United States](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146). Coinciding with this diversification of employment was a diversification in the source of where people in Mexico who came to the U.S. originated from: instead of coming mainly from rural Mexico, [all economically disadvantaged regions had people coming to the U.S](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146). With all of this history in mind, I wanted to try to find out if this manifested at all in the origins of Mexicans in different U.S. cities. Are there more people from urban Mexico in New York City than in a more traditional Mexican immigration stronghold like San Francisco?

### Project Goals
How does this project determine the home regions of Mexicans in the United States? Through the outward representations of Mexican restaurants in American cities with a large hispanic population. Using a database of cities and terms that refer to specific regions of Mexico, I connect the words in Mexican restaurant names to regions of Mexico. In this way, I am capturing a subset of the population, but hopefully one that unbiasedly and fairly captures characteristics of the total population in the cities discussed here. It is my hope that **by analyzing the restaurant names we can learn more about the origin of Mexican immigrants in the United States**.

### Results
We see noticable differences in the proportion of the regions referred to in restaurant names for each of these cities. Many more people in NYC are from Puebla ([_Mixteca Baja_](https://en.wikipedia.org/wiki/La_Mixteca)) in NYC than we do in any of the other cities measured. Similarly, _40_% of San Francisco Mexican restaurants are from the Guanajuato region, the next closest has 1%. Additionally, we see that Chicago is very diverse in where their Mexican restaurants originate from (possibly because of the low count of restaurants) whereas Dallas is much more concentrated in the home region of their restaurants. Taken together, this gives partial evidence to the view that more traditional Mexican-emigreé regions in the U.S. (San Francisco, Dallas) have a more diverse Mexican population than relatively new Mexican-emigreé regions in the U.S. (New York City, Chicago). 

![Mexican Regions for Each City](/Map_of_regions_from_all_cities.png)

Although not expected, we also see strong evidence of chain migration to specific regions, and even neighborhoods, of the United States. In New York City, we see 5 of the 86 restaurants refer to one <10,000 person town in Mexico ([Tulcingo](https://es.wikipedia.org/wiki/Municipio_de_Tulcingo)). It may even be that more people from Tulcingo del Valle, Puebla, Mexico live in NYC than in the town itself! It is almost certain that the people from Tulcingo in NYC are part of a tight-knit community that encouraged each other to move to NYC. 

### Shortcomings
This project is suggestive, but should not be taken as fact or proof concerning Mexican regional migration to the United States. Crucially, this project rests on the assumption that 1. People from different regions of Mexico will set up restaurants in about equal proportion and 2. People from different regions of Mexico will display their regional identity in their restaurant names in about equal proportion. Both of these are untested and could potentially be incorrect. Additionally, if employment opportunities for Mexicans are different in the four cities studied, then perhaps there will be far fewer restaurants and more laborers (Chicago certainly appears that way). Hopefully by looking at the percentage of all region-referring Mexican restaurants, this problem is reduced. Moreover, there is the problem of the officialness of restaurants: what I was able to find from city food inspection data likely under-represents the true number of restaurants in these cities. Last, the matching of the restaurant names has a few problems. For one, the matches themselves were sometimes questionable: originally, "Jalisco" was connected to "Mexico City", instead of the region "Jalisco" (this was corrected). There were about 20,000 entries, so it was impossible to control for all errors. More commonly, there is the judgment call of determining if a word in a restaurant name is referring to a specific city in Mexico. Some restaurants had "alamo" in their name, does this refer to a village in Tabasco, a poplar tree (its translation) or the alamo in Texas? I had to make judgment calls to all of these cases. The data is available in case someone more familiar with Mexico and these restaurants cares to correct me. Regardless, they should have a relatively small effect on the percentage of restaurants being pegged to specific regions in Mexico. 

## Technologies Used
- Jupyter Notebook
- Python
    - Pandas
    - Folium
    - GeoPandas
    - Shapely
    - Unidecode146
