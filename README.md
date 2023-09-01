# Genomic Analytics Tool (gnat)
## Tool describtion: 
GNAT is a python Fet supported desktop App developed by Intechgambit to process genomic data (DNA and Edna) by pulling data from [NCBI Entrez databased](https://www.ncbi.nlm.nih.gov/search/) utlizing the Entrez API, creating a custom blast supported database, making taxonmic assignments and annonotations and generating analytics and vizulizations. The tool also does data conversion to the FASTA format that is searchable by NCBI BLAST.
## NCBI Entrez API downloads:
Downloads from NCBI Entrez databases is used independently or in combination of the user's own datasets to create a searchable BLAST and relational database that can be used for annotations and taxonomic assignments. 
### How to use the feature
Borads referred to as "Species Boards" in the tools are utilized to create search parameters used to retrieve data from NCBI databases through their [Entrez API](https://www.ncbi.nlm.nih.gov/books/NBK25501/).
- Launch the gnat app
- Go from Workspace, select Board Manager. This will take you to home of species boards
- You can either create a new board clicking on Add new board or use an existing board by clicking on it.
- Enter a species name that you will searching. This will be used to save all the output activivties for that list.You have options to select different colors for your lists or you can leave at a defaulst. After typing the name you can click create or enter.
- Add a search query for your list. Search queries are parameters used directly to search the NCBI databases. You can add multiple search queries on a single list. Each list contutes a single search and items on the list are searched iteratively. Each search query should include all the parameters you want to apply on that specific search. If you do not know how to generate queries for NCBI database search you can generate them by going to [NCBI website](https://www.ncbi.nlm.nih.gov). Select the Nucleotide database and use a desired search term. Apply all the filters needed and copy the "Search details" contents and paste it search detail of the tool to add as a query.
- Click on the three dots in the right corner of the list you created. Edit options allows you to edit the name you entered for the list. Delete option will delete the list. Get date will search your queries against the NCBI Entrez database and download the data to your local machine.
