# Mexican Immigration Through Restaurant Names

## Description
Mexican immigration to the United States has a long and interesting history. The origin and destination of Mexican immigrants in the U.S. is a somewhat open question that has not received the attention it deserves. In this project, **I aim to discover more about the home regions of Mexicans in 4 major cities with a significant Mexican-heritage population: New York City, Chicago, Dallas and San Francisco**. 

### Historical Background
Mexican Immigration to the United States is [generally characterized](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146) by (economic) _pull_ factors to the United States with certain periods of Mexican history creating _push_ factors for migration. Traditionally, Mexican men worked in [agriculture in the American Southwest](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146) and waited until the next harvest either by returning to Mexico or temporarily living in nearby U.S. cities. Starting in the 80's this paradigm shifted: since the border was becoming hard, if someone wanted to work in the U.S., they needed to remain. This being the case, after someone in the family established themselves, they then brought their family into the United States. Work also moved to cities with the lesser need and pay for farm work in comparison to low-wage jobs in cities. This led to a diversification in the home regions or Mexican immigrants, instead of coming mainly from rural Mexico, [all economically disadvantaged regions had people coming to the U.S](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146).

Since there is a difference in these periods of Mexican immigration to the U.S. and differences in primary destination within the U.S., I wonder: Do more traditional destinations in the American Southwest significantly differ from newer destinations? Specifically, does San Francisco have more people from certain regions than New York City? Do the newer destinations of Chicago and New York City share similarities? What about the more traditional destinations in San Francisco and Dallas? 

### Project Goals
This project aimed to use the outward representations of Mexican restaurants in American cities with a large Mexican population to determine the home origins of these immigrants. If many restaurant names featured references to a certain region, the owner(s) and/or some people who work at that restaurant are certainly from that region. In either case, the region associated with that restaurant is meant to attract customers. Using a database of cities and terms that refer to specific regions of Mexico, I connect the words in Mexican restaurant names to those regions. In this way, I am capturing a subset of the population, but hopefully one that unbiasedly and fairly captures characteristics of the total population in the cities discussed here. It is my hope that **by analyzing the restaurant names we can learn more about the origin of Mexican immigrants in the United States**.

### Results
We see noticable differences in the proportion of the regions referred to in restaurant names for each of these cities. Over 46% of NYC restaurants are connected to Puebla ([_Mixteca Baja_](https://en.wikipedia.org/wiki/La_Mixteca)), a percentage of restaurants that is far higher than we see in any of the other cities measured. The next closes is  Michoacàn which makes up _31_% of Dallas's Mexican restaurants. Overall, we see the lack of a clear pattern in which regions Mexicans come from and where they end up in the United States. The tendencies that emerge are a few cases of clear connections between Mexican regions and American cities (Michoacàn to San Francisco and Dallas, Puebla to New York City) but a generally balanced migration from all parts of Mexico to the United States.

![Mexican Regions for Each City](./images/Map_of_cities_and_their_regions_cont_scale.png)

Although not expected, we also see strong evidence of chain migration to specific regions, and even villages, of the United States. In New York City, we see 5 of the 79 restaurants refer to one <10,000 person town in Mexico ([Tulcingo](https://es.wikipedia.org/wiki/Municipio_de_Tulcingo)). It may even be that more people from Tulcingo del Valle, Puebla, Mexico live in NYC than in the town itself! It is almost certain that the people from Tulcingo in NYC are part of a tight-knit community that encouraged each other to move to NYC. 

Overall, the regions represented mirror those regions that receive the most remittances from Mexicans living in the United States. In both cases, we see that most of the Mexicans living in the U.S. come from Central Mexico. In particular, the mainly rural regions on the Pacific coast of Central Mexico (Jalisco, Michoacàn, etc.) are well represented. This commonality leads me to believe that this method is a fruitful one in determining the origins of Mexicans living in the U.S.

![Mexican Regions Represented and Remittances](./images/Regions_represented_plus_remittances_pct2.png)

### Shortcomings
This project is suggestive, but should not be taken as fact or proof concerning Mexican regional migration to the United States. Crucially, this project rests on the assumption that 
    1. People from different regions of Mexico will set up restaurants in about equal proportion and 
    2. People from different regions of Mexico will display their regional identity in their restaurant names in about equal proportion. 
Both of these are untested and could be incorrect. Additionally, if employment opportunities for Mexicans are different in the four cities studied, then perhaps there will be far fewer restaurants and more laborers (Chicago and San Francisco certainly appear that way). Hopefully by looking at the percentage of all region-referring Mexican restaurants, this problem is reduced. Moreover, there is the problem of the officialness of restaurants: what I was able to find from city food inspection data likely under-represents the true number of restaurants in these cities. Last, matching the restaurant names to restaurants has a few problems. For one, the matches themselves were sometimes questionable: originally, "Jalisco" was connected to "Mexico City", instead of the region "Jalisco" (this was corrected). There were about 20,000 entries, so it was impossible to control for all errors. More commonly, there is the judgment call of determining if a word in a restaurant name is referring to a specific city in Mexico. Some restaurants had "alamo" in their name, does this refer to a village in Tabasco, a poplar tree (its translation) or the alamo in Texas? I decided which region matching words were legitimate by searching for each term on wikipedia and make a judgment call. The data is available in case someone more familiar with Mexico and these restaurants cares to correct me. Regardless, they should have a relatively small effect on the percentage of restaurants being pegged to specific regions in Mexico. 

## Technologies Used
- Jupyter Notebook
- Python
    - Pandas
    - Folium
    - GeoPandas
    - Shapely
    - Unidecode146
    - wikipedia 
    - Seaborn
    - Matplotlib

## Further Reading
The results of this project were published in a two-part series of blogs ([Part 1](https://gregfeliu.medium.com/what-can-we-learn-about-mexican-immigration-from-restaurant-names-part-1-57165263915f), [Part 2](https://gregfeliu.medium.com/what-can-we-learn-about-mexican-immigration-from-restaurant-names-part-2-412aa86e1302)). Further, a [Spanish-language article](https://eldiariony.com/2021/03/12/cual-es-la-region-mexicana-preferida-de-los-restaurantes-en-nueva-york-y-estados-unidos/) of this project was written in El Diario NYC.  

## Update
In March 2021 I redid this project. I streamlined my demonym dictionary, added more restaurant categories for Chicago (which led to 50.6 times more restaurants being found), and lowered the size of my code (overall, the code is 8 times smaller now than it was in the first iteration). 
