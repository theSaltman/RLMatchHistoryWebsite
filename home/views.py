from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Csv
from django.contrib.auth.models import User
import csv

def home(request):
	obj = Csv.objects.all()
	
	totalAssists=0
	totalDemos=0
	totalGoals=0
	totalMVP=0
	highestRankedMMR=0
	highestCasualMMR=0	
	highestPoints=0
	totalSaves=0
	totalShots=0
	totalWins=0
	totalLosses=0
	totalGames=0
	winPercent=0.0
	rankedWinPercent=0.0
	casualWinPercent=0.0
	totalRankedWins=0
	totalCasualWins=0
	totalRankedGames=0
	totalCasualGames=0
	totalMostGoalsInAGame=0
	
	assists = []
	demos = []
	goals = []
	mmr = []
	playlist = []
	mvp = []
	points = []
	saves = []
	shots = []
	wins = []
	ranked = []
	myTeamGoals = []	
	
	mostAssists=0
	mostDemos=0
	mostGoals=0
	mostMVP=0
	mostSaves=0
	mostShots=0
	mostWins=0
	mostLosses=0
	mostGames=0
	highestWinPercent=0.0
	highestRankedWinPercent=0.0
	highestCasualWinPercent=0.0
	mostRankedWins=0
	mostCasualWins=0
	mostRankedGames=0
	mostCasualGames=0

	mostAssistsAuthor=''
	mostDemosAuthor=''
	mostGoalsAuthor=''
	highestRankedMMRAuthor=''
	highestRankedMMRPlaylist=''
	highestCasualMMRAuthor=''
	mostMVPAuthor=''
	highestPointsAuthor=''
	highestPointsPlaylist=''
	mostSavesAuthor=''
	mostShotsAuthor=''
	mostWinsAuthor=''
	mostLossesAuthor=''
	mostGamesAuthor=''
	highestWinPercentAuthor=''
	highestRankedWinPercentAuthor=''
	highestCasualWinPercentAuthor=''
	mostRankedWinsAuthor=''
	mostCasualWinsAuthor=''
	mostRankedGamesAuthor=''
	mostCasualGamesAuthor=''
	mostGoalsInAGamePlaylist=''
	mostGoalsInAGameAuthor=''
		
	for item in obj:
		with open(item.file_name.path, 'r') as f:
			totalAssists=0
			totalDemos=0
			totalGoals=0
			totalMVP=0
			totalSaves=0
			totalShots=0
			totalWins=0
			totalLosses=0
			totalGames=0
			totalRankedWins=0
			totalCasualWins=0
			totalRankedGames=0
			totalCasualGames=0

			assists = []
			demos = []
			goals = []
			mmr = []
			playlist = []
			mvp = []
			points = []
			saves = []
			shots = []
			wins = []
			ranked = []
			myTeamGoals = []	
			
			reader = csv.reader(f, delimiter=',')
			for i, row in enumerate(reader):
				if i==0:
					pass
				else:
					assists.append(int(row[0]))
					demos.append(int(row[1]))
					goals.append(int(row[2]))
					mmr.append(int(row[3]))
					mvp.append(int(row[4]))
					myTeamGoals.append(int(row[5]))
#					otherteamgoals[i]=row[6]
					playlist.append(row[7])
					points.append(int(row[8]))
					ranked.append(int(row[9]))
					saves.append(int(row[10]))
					shots.append(int(row[11]))
#					time[i]=row[12]
#					timstamp[i]=row[13]
					wins.append(int(row[14]))
					totalGames += 1
					
			for i in range(0,totalGames):
				totalAssists += assists[i]
				totalDemos += demos[i]
				totalGoals += goals[i]
				totalMVP += mvp[i]
				totalSaves += saves[i]
				totalShots += shots[i]
				totalWins += wins[i]
				if mmr[i] > highestRankedMMR and ranked[i] is 1:
					highestRankedMMR = mmr[i]
					highestRankedMMRPlaylist = playlist[i]
					highestRankedMMRAuthor = item.author
				if mmr[i] > highestCasualMMR and ranked[i] is 0:
					highestCasualMMR = mmr[i]
					highestCasualMMRAuthor = item.author
				if points[i] > highestPoints:
					highestPoints = points[i]
					highestPointsPlaylist = playlist[i]
					highestPointsAuthor = item.author
				if wins[i] == 0:
					totalLosses += 1
				if wins[i] == 1 and ranked[i] == 1:
					totalRankedWins += 1
				if wins[i] == 1 and ranked[i] == 0:
					totalCasualWins += 1
				if ranked[i] == 1:
					totalRankedGames += 1
				else:
					totalCasualGames += 1
				if myTeamGoals[i] > totalMostGoalsInAGame:
					totalMostGoalsInAGame = myTeamGoals[i]
					mostGoalsInAGamePlaylist = playlist[i]
					mostGoalsInAGameAuthor = item.author
			if totalGames is 0:
				winPercent = 0.0
			else:
				winPercent = round((totalWins/totalGames) * 100, 2)
			if totalRankedGames is 0:
				rankedWinPercent = 0.0
			else:
				rankedWinPercent = round((totalRankedWins/totalRankedGames) * 100, 2)
			if totalCasualGames is 0:
				casualWinPercent = 0.0
			else:
				casualWinPercent = round((totalCasualWins/totalCasualGames) * 100, 2)
			if totalAssists >= mostAssists:
				mostAssists = totalAssists
				mostAssistsAuthor = item.author
			if totalDemos >= mostDemos:
				mostDemos = totalDemos
				mostDemosAuthor = item.author
			if totalGoals >= mostGoals:
				mostGoals = totalGoals
				mostGoalsAuthor = item.author
			if totalMVP >= mostMVP:
				mostMVP = totalMVP
				mostMVPAuthor = item.author
			if totalSaves >= mostSaves:
				mostSaves = totalSaves
				mostSavesAuthor = item.author
			if totalShots >= mostShots:
				mostShots = totalShots
				mostShotsAuthor = item.author
			if totalWins >= mostWins:
				mostWins = totalWins
				mostWinsAuthor = item.author
			if totalLosses >= mostLosses:
				mostLosses = totalLosses
				mostLossesAuthor = item.author
			if totalGames >= mostGames:
				mostGames = totalGames
				mostGamesAuthor = item.author
			if winPercent >= highestWinPercent:
				highestWinPercent = winPercent
				highestWinPercentAuthor = item.author
			if rankedWinPercent >= highestRankedWinPercent:
				highestRankedWinPercent = rankedWinPercent
				highestRankedWinPercentAuthor = item.author
			if casualWinPercent >= highestCasualWinPercent:
				highestCasualWinPercent = casualWinPercent
				highestCasualWinPercentAuthor = item.author
			if totalRankedWins >= mostRankedWins:
				mostRankedWins = totalRankedWins
				mostRankedWinsAuthor = item.author
			if totalCasualWins >= mostCasualWins:
				mostCasualWins = totalCasualWins
				mostCasualWinsAuthor = item.author
			if totalRankedGames >= mostRankedGames:
				mostRankedGames = totalRankedGames
				mostRankedGamesAuthor = item.author
			if totalCasualGames >= mostCasualGames:
				mostCasualGames = totalCasualGames
				mostCasualGamesAuthor = item.author

	context = {
		'title': 'Home',
		'posts': obj, #changed Post.objects.all() to Csv
		'mostAssists': mostAssists,
		'mostAssistsAuthor': mostAssistsAuthor,
		'mostDemos': mostDemos,
		'mostDemosAuthor': mostDemosAuthor,
		'mostGoals': mostGoals,
		'mostGoalsAuthor': mostGoalsAuthor,
		'highestRankedMMR': highestRankedMMR,
		'highestRankedMMRPlaylist': highestRankedMMRPlaylist,
		'highestRankedMMRAuthor': highestRankedMMRAuthor,
		'highestCasualMMR': highestCasualMMR,
		'highestCasualMMRAuthor': highestCasualMMRAuthor,
		'mostMVP': mostMVP,
		'mostMVPAuthor': mostMVPAuthor,
		'highestPoints': highestPoints,
		'highestPointsAuthor': highestPointsAuthor,
		'highestPointsPlaylist': highestPointsPlaylist,
		'mostSaves': mostSaves,
		'mostSavesAuthor': mostSavesAuthor,
		'mostShots': mostShots,
		'mostShotsAuthor': mostShotsAuthor,
		'mostWins': mostWins,
		'mostWinsAuthor': mostWinsAuthor,
		'mostLosses': mostLosses,
		'mostLossesAuthor': mostLossesAuthor,
		'mostGames': mostGames,
		'mostGamesAuthor': mostGamesAuthor,
		'highestWinPercent': highestWinPercent,
		'highestWinPercentAuthor': highestWinPercentAuthor, 
		'highestRankedWinPercent': highestRankedWinPercent,
		'highestRankedWinPercentAuthor': highestRankedWinPercentAuthor, 
		'highestCasualWinPercent': highestCasualWinPercent,
		'highestCasualWinPercentAuthor': highestCasualWinPercentAuthor, 
		'mostRankedWins': mostRankedWins,
		'mostRankedWinsAuthor': mostRankedWinsAuthor,
		'mostCasualWins': mostCasualWins,
		'mostCasualWinsAuthor': mostCasualWinsAuthor,
		'mostRankedGames': mostRankedGames,
		'mostRankedGamesAuthor': mostRankedGamesAuthor,
		'mostCasualGames': mostCasualGames,
		'mostCasualGamesAuthor': mostCasualGamesAuthor,
		'totalMostGoalsInAGame': totalMostGoalsInAGame,
		'mostGoalsInAGamePlaylist': mostGoalsInAGamePlaylist,
		'mostGoalsInAGameAuthor': mostGoalsInAGameAuthor,
		
	}
	return render(request, 'home/home.html', context)
	
def about(request):
	return render(request, 'home/about.html', {'title': 'About'}) #testing title

def search(request):
	users = User.objects.all()
	object_list = None
	def get_queryset(self): # new
		query = self.request.GET.get('q')
		object_list = User.objects.filter(
			Q(username__icontains=query)
		)
		print("printing object_list")
		print(object_list)
		#return object_list	
	
	context = {
		'title': 'Search',
		'users': users,
		'object_list': object_list,
	}
	return render(request, 'home/search.html', context)
