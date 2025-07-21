'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Demonstrate method overriding and polymorphism using VideoPlayer and MP4 classes
'''

class VideoPlayer:
    def play(self):
        print(f'VideoPlayer Play()')
 
class MP4(VideoPlayer):
    def play(self):
        print(f'MP4 Play()')
 
if __name__ == '__main__':
    plays = [VideoPlayer(), MP4(), MP4(), VideoPlayer(), VideoPlayer(), MP4()]
    for obj in plays:
        obj.play()
