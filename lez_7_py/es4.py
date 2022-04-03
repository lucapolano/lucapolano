import numpy as np
import os
class campionato_sportivo():

    def _init_(self):

        os.chdir('/home/runner/lucapolano-7/lez_7_py')
        team = list(open( 'serie_a.txt', 'r'))
        for i in range(len(team)-1):
            team[i] = team[i][:-1]

        punti = list(np.loadtxt('punti.txt'))
        for i in range(len(punti)):
            punti[i] = int(punti[i])

        self.classifica = list(zip(team, punti))


    def promoz_retrocess(self):

        #---remove team---

        team, punti = zip(*self.classifica)
        team, punti = list(team), list(punti)
        team_retr = input('Squadra da eliminare: ')

        if team_retr in team:
            ind_del = team.index(team_retr)
            p_del = punti[ind_del]
            team.remove(team_retr)
            punti.remove(p_del)
            self.classifica = list(zip(team, punti))

        else:
            print('Not valid')

        #---add team---
        team_pro = input('Squadra da aggiungere: ')
        if team_pro == 'None' or team_pro == 'Nessuna':
            self.classifica = list(zip(team, punti))

        else:
            punti_pro = int(input('Punti nuova squadra: '))
            team.append(team_pro)
            punti.append(punti_pro)
            self.classifica = list(zip(team, punti))

    def winner_losers(self):

        team, punti = zip(*self.classifica)
        team, punti = list(team), list(punti)

        p_max = np.max(punti)
        win_team = team[punti.index(p_max)]

        p_min = np.min(punti)
        los_team = team[punti.index(p_min)]

        punti.remove(p_min)
        p_min2 = np.min(punti)
        los_team2 = team[punti.index(p_min2)]

        punti.remove(p_min2)
        p_min3 = np.min(punti)
        los_team3 = team[punti.index(p_min3)]


        return 'The winner is:', win_team, 'with points', p_max ,'The losers are:', los_team, los_team2, los_team3 , 'with points respectively', p_min, p_min2, p_min3

cs = campionato_sportivo()
cs._init_()
cs.promoz_retrocess()
print(cs.winner_losers())