from typing import Optional
import os
welcome=["welcome test"]
bio=["bio test"]
class CHANGE(wt, bio, welcome):    
  def init(self, wt, bio, welcome):
    self.wt=wt
    self.bio=bio
    self.welcome=welcome
  
  def FIND_COMMAND(self, commands, y, x):
    command=str(commands).lower()
    if command == "welcome":
      self.MAIN_SCRIPT(1, command, self.welcome, x)
    elif command == "bio":
      self.MAIN_SCRIPT(1, command, self.bio, x)
    elif command == "wt":
      return
    else:
      return
  
  def git(self):
    os.system('./git_clone.sh')
  
  def CHANGE_ARRAY(self, y, x):
    y.remove(y[-1])
    y.append(x)
    print(y[-1])
    self.git()
  
  def MAIN_SCRIPT(self, z: Optional[int], command, y, x: str): 
    if z==0:
      self.FIND_COMMAND(command, y, x)
      return
    elif z==1:
      print(y[-1])
    elif z==2:
      print(y[-1])
    if z != 0 or z != None:
      return self.CHANGE_ARRAY(y, x)
