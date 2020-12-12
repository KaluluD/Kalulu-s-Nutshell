Name: Lujia Deng
NetID: ld781

Thank you for reviewing my visualization project on 'Looking into League of Legends Season 2020. Here are some notes to help you understand files in this folder:

================================================

0_storyboard.Rmd: It generates the flexdashboard that serves as the main presentation of this project. To look at the dashboard, you can directly go to 0_storyboard.html

1_leagueMap.Rmd: It produces the map visualization.

2_win-rate_3_league-stats_4_team_time_series.ipynb: This is the jupyter notebook that produces the win rate plot (bar plot), league game style comparison plots (ridgeline plot), and the top team game style over time plot (time series plot).

5_championNetwork.Rmd: It produces the champion networks

6_word_cloud.Rmd: It produces the word cloud.

Each rmarkdown file is accompanied with a generated html file. If you want to have a quick look at the resulted visualizations, you can directly look at the html files.

================================================

Data used by this project is in the data_folder. Twitter data collecting and network data preprocessing scripts are also in that folder.

================================================

The flexdashboard uses pre-generated graphs in the png format, stored in this folder to creates the final product. I chose to pre-generate graphs, instead of putting the source code in the flexdashboard file mainly due to various imcompatibility between the ways that I code those visualizations and flexdashboard, including but not limited to visualization 2,3,4, which are coded in Python as well as the word cloud, a html widget generated with the "wordcloud2" r library and I failed to render it in with flexdashboard. Apologize for creating inconvenience for you. I greatly appreciate your understanding.
 
================================================

If you have any questions, please reach out to ld781@georgetown.edu. Thanks again for your time and help!