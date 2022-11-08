#Name:  Ahmad Alrafati
#Email: ahmad.alrafati96@myhunter.cuny.edu
#Date: october 23, 2022
#This program Writes a function, computePrice(), that takes two parameters: liquid (string) and the size type (string)





def computePrice(liquid, size):
    order = {
        'coffee':{
            'small':2.5,
            'medium':2.75,
            'large':3.0
        },
        'misto':{
            'small':3.15,
            'medium':3.35,
            'large':3.7
        },
        'mocha':{
            'small':3.5,
            'medium':3.8,
            'large':4.25
        },
        'tea':{
            'small':2.35,
            'medium':2.45,
            'large':2.90
        }
        
    }
    try:
        return order[liquid][size]
    except:
        return -1
