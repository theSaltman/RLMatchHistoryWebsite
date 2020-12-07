from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Csv
import csv


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created, time to login!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form}) 

@login_required
def profile(request, pk=None):
	obj = Csv.objects.all()
	highestRankedMMR=0
	highestCasualMMR=0	
	highestPoints=0
	
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
	winsStr = []
	results = []
	ranked = []
	rankedStr = []
	timestamp = []
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
	winPercent=0
	rankedWinPercent=0
	casualWinPercent=0
	mostRankedWins=0
	mostCasualWins=0
	mostRankedGames=0
	mostCasualGames=0
	mostGoalsInAGame=0
	
	highestMMRPlaylist=''
	highestPointsPlaylist=''
	mostGoalsInAGamePlaylist=''

	for item in obj:
		if item.author.pk == pk:
			user = item.author
			with open(item.file_name.path, 'r') as f:
				reader = csv.reader(f, delimiter=',')

				for i, row in enumerate(reader):
					if i==0:
						pass
					else:
						#row = " ".join(row)
						#row = row.split()
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
						if int(row[9]) == 1:
							rankedStr.append('Ranked')
						else:
							rankedStr.append('Casual')
						saves.append(int(row[10]))
						shots.append(int(row[11]))
	#					time[i]=row[12]
						timestamp.append(row[13])
						wins.append(int(row[14]))
						if int(row[14]) is 1:
							winsStr.append('Win')
						else:
							winsStr.append('Loss')
						mostGames += 1
						
				for i in range(0,mostGames):
					mostAssists += assists[i]
					mostDemos += demos[i]
					mostGoals += goals[i]
					mostMVP += mvp[i]
					mostSaves += saves[i]
					mostShots += shots[i]
					mostWins += wins[i]
					if mmr[i] > highestRankedMMR and ranked[i] is 1:
						highestRankedMMR = mmr[i]
						highestMMRPlaylist = playlist[i]
					if mmr[i] > highestCasualMMR and ranked[i] is 0:
						highestCasualMMR = mmr[i]
					if points[i] > highestPoints:
						highestPoints = points[i]
						highestPointsPlaylist = playlist[i]
					if wins[i] == 0:
						mostLosses += 1
					if wins[i] == 1 and ranked[i] == 1:
						mostRankedWins += 1
					if wins[i] == 1 and ranked[i] == 0:
						mostCasualWins += 1
					if ranked[i] == 1:
						mostRankedGames += 1
					else:
						mostCasualGames += 1
					if myTeamGoals[i] > mostGoalsInAGame:
						mostGoalsInAGame = myTeamGoals[i]
						mostGoalsInAGamePlaylist = playlist[i]
				if mostGames == 0:
					winPercent = 0
				else:
					winPercent = round((mostWins/mostGames) * 100, 2)
				if mostRankedGames == 0:
					rankedWinPercent = 0
				else:
					rankedWinPercent = round((mostRankedWins/mostRankedGames) * 100, 2)
				if mostCasualGames == 0:
					casualWinPercent = 0
				else:
					casualWinPercent = round((mostCasualWins/mostCasualGames) * 100, 2)
				things = []
				stuff = {}
				for i in reversed(range(0,mostGames)):
					stuff = {"goals": goals[i], "assists": assists[i], "mmr": mmr[i], "playlist": playlist[i], "mvp": mvp[i], "points": points[i], "saves": saves[i], "shots": shots[i], "wins": winsStr[i], "ranked": rankedStr[i], "timestamp": timestamp[i]}
					things += [stuff]
	context = {
		#'title': "Profile",
		'title': "Profile - " + str(user),
		'userCSV': results,
		'mostAssists': mostAssists,
		'mostDemos': mostDemos,
		'mostGoals': mostGoals,
		'highestRankedMMR': highestRankedMMR,
		'highestMMRPlaylist': highestMMRPlaylist,
		'highestCasualMMR': highestCasualMMR,
		'mostMVP': mostMVP,
		'highestPoints': highestPoints,
		'highestPointsPlaylist': highestPointsPlaylist,
		'mostSaves': mostSaves,
		'mostShots': mostShots,
		'mostWins': mostWins,
		'mostLosses': mostLosses,
		'mostGames': mostGames,
		'winPercent': winPercent,
		'mostRankedWins': mostRankedWins,
		'mostCasualWins': mostCasualWins,
		'mostRankedGames': mostRankedGames,
		'mostCasualGames': mostCasualGames,
		'rankedWinPercent': rankedWinPercent,
		'casualWinPercent': casualWinPercent,
		'mostGoalsInAGame': mostGoalsInAGame,
		'mostGoalsInAGamePlaylist': mostGoalsInAGamePlaylist,
		'things': things,	
		'range': range(0,mostGames),
		'user': user,

	}
	return render(request, 'users/profile.html', context)
