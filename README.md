# candidate-wordcloud
Generate wordclouds from the websites of political candidates.

## Instructions

### Single url version

1. Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mbonsma/candidate-wordcloud/HEAD) to launch the interactive notebook. Once it loads, double-click on the file called `candidate_wordcloud.ipynb` in the left pane. This will open an interactive notebook in your browser.
2. Get the URL for a candidate you are interested in. Ideally, find a page that has policy or platform information on it (this is usually called something like "priorities" or "platform").
3. Paste the URL inside the quotes in the first box, and type a name to save your finished wordcloud under.
4. In the top-left menu "Run", choose "Run all cells". Alternatively, click the double-arrow button (>>) in the top bar above the notebook. This runs the code and hopefully generates a nice wordcloud for your candidate! 
5. The finished wordcloud will be saved in the interactive folder; to download it, find the filename in the left pane, right-click, and choose 'Download'.

### Batch url version

Use the batch version if you want to create multiple wordclouds for different URLs, OR you want to create a single wordcloud with several URLs. This script handles both cases. 

To use the batch version, you will need a csv with a list of URLs called `url_list.csv`, formatted like this:

| url | language | save_name |
| --- | -------- | --------- |
| person1.com | en | person1 |
| person1_platform.com | en | person1 |
| person2_about.com | fr | person2 |
| person2_priorities.com | fr | person2 |

Language can be 'en' (English) 'fr' (French), or 'all' (both English and French). This determines the list of words that are automatically removed from the wordcloud. 

If you want multiple URLs combined in a single wordcloud, make sure that the 'language' and 'save_name' fields are the same for each URL you want combined. The script groups queries by language and save name. 

1. Click [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mbonsma/candidate-wordcloud/HEAD) to launch the interactive notebook. Once it loads, double-click on the file called `candidate_wordcloud_batch.ipynb` in the left pane. This will open an interactive notebook in your browser.
2. Upload your list of URLs by dragging and dropping it in the left file browser pane.
3. In the first cell, enter the filename of your list of URLs.
4. In the top-left menu "Run", choose "Run all cells". Alternatively, click the double-arrow button (>>) in the top bar above the notebook. This runs the code and hopefully generates a nice wordcloud for your candidate! 
5. The finished wordclouds will be saved in the interactive folder; to download them, find the filenames in the left pane, right-click, and choose 'Download'.

