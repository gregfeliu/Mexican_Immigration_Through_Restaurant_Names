# Mexican Immigration Through Restaurant Names

## Description
Mexican immigration to the United States has a long and interesting history. There are 4 major periods to this migration that have led to the distribution of people of Mexican descent to where they live today. In this project, **I aim to discover more about the distribution of Mexicans in 4 major cities with a significant Mexican-heritage population: New York City, Chicago, Dallas and San Francisco**. 

### Historical Background
Mexican Immigration to the United States is [generally characterized by _pull_ factors to the United States with certain periods of Mexican history creating _push_ factors for migration with the constant theme of poverty pushing them northward](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146). Traditionally, Mexican men worked in agriculture in the American Southwest and waited until the next harvest either by returning to Mexico or temporarily living in nearby U.S. cities. It wasn't until the Great Depression where anti-immigrant sentiment started making this porous U.S.-Mexico border into a firm one. This theme continued until the relatively firm border that we have today. Starting in World War 2, Mexican labor was needed to fill the gaps in rural labor left by the war. Thereafter, Mexican labor began diversifying and moving beyond the American Southwest. This was even more so after the Immigration Control and Reform Act of 1986 (IRCA). This law aimed to end illegal immigration by granting citizenship to all Mexican immigrants who arrived pre-1982. This led to thos already in the U.S. to bring their families and seek out a life in the United States (https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146). Coinciding with this diversification of employment was a diversification in the source of where people in Mexico who came to the U.S. originated from: instead of coming mainly from rural Mexico, [all economically disadvantaged regions had people coming to the U.S](https://oxfordre.com/americanhistory/view/10.1093/acrefore/9780199329175.001.0001/acrefore-9780199329175-e-146). With all of this history in mind, I wanted to try to find out if this manifested at all in the origins of Mexicans in different U.S. cities. Are there more people from urban Mexico in New York City than in a more traditional Mexican immigration stronghold like San Francisco?

### Project Goals
How does this project determine the home regions of Mexicans in the United States? Through the outward representations of Mexican restaurants in American cities woth a large hispanic population. Using a database of cities and terms that refer to specific regions of Mexico, I connect the words in Mexican restaurant names to regions of Mexico. In this way, I am capturing a subset of the population, but hopefully one that unbiasedly and fairly captures characteristics of the total population in the cities discussed here. It is my hope that by analyzing the 

### Results
We see noticable differences in the proportion of the regions referred to in restaurant names for each of these cities. More people in NYC are from Puebla and Oaxaca ([_Mixteca Baja_](https://en.wikipedia.org/wiki/La_Mixteca)) in NYC than we do in any of the other cities measured.  





This was my final project at Flatiron Data Science Bootcamp. Here, **I aim to find all acoustic vowels in an unmarked audio file of natural conversational speech**. By doing so, one would be able to use this as a basis for an Automatic Speech Recognition system and could be used to identify languages or be used in phonetic research. 

The data originally came from a [study](http://groups.linguistics.northwestern.edu/speech_comm_group/wildcat/) done by Northwestern University Linguistics Department. The [transcriptions](https://speechbox.linguistics.northwestern.edu/wildcat/#!/recordings) were auto-aligned from transcriptions and hand corrected by the studies' authors. This was further hand-corrected by me in order to only include _acoustic_ vowels, not phonemic ones. For example, the first _e_ in "interesting" is often acoustically absent (there is a "ch" sound, not "ter"). In the original transcription the "e" sound will be marked, even if not actually present, my corrections fixed this. 

I investigate the effectiveness of three different approaches in this project: 
- **[Hampel Filter](https://dsp.stackexchange.com/questions/26552/what-is-a-hampel-filter-and-how-does-it-work)**: One finds the median volume of a small section of the audio file, and determines if the sample in question is above a threshold of standard deviations of that median volume. 
- **Neural Network**: Feeds the model frames of vowels and performs a 2D vanilla neural network to find vowels in the test data.
- **Combination Model**: This model combines the results of the previous two models to hopefully obtain more accurate predictions.

## Results
The Neural Network model and Combination model both performed equally well. The Hampel Filter had a significantly lower effectiveness than the other two approaches. Since there is little if any gain from using a combination model, a 2D neural network is the best approach used here.

## Technologies Used
- Jupyter Notebook
- Python
    - Pandas
    - os
    - re
    - SciPy
    - NumPy