from distutils.command.clean import clean
from http import client
import profile
import tkinter as tk
from urllib import response
import boto3

root=tk.Tk()
root.geometry("400x240")
root.title("T2S-Con Amazon Polly")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
      aws_mag_con=boto3.session.session(profile_name='20bcs320_user')
      client=aws_mag_con.client(service_name='polly',region_name='us-east-1')
      result=textExample.get("1.0","end")
      print(result)
      response=client.synthesize_speech(VoiceId='Joanna',OutputFormat='mp3',Text=result,Engine='neural')
      print(response)
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()
