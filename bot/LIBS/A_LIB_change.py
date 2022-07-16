from typing import Optional
import os
import sys
sys.path.append("..")
from extras.text_zone import BIG
class CHANGE():    
  def init(self):
    self.wt=BIG.WT
    self.bio=BIG.bio
    self.welcome=BIG.welcome_dm
  
  def FIND_COMMAND(self, commands, y, x):
    command=str(commands).lower()
    if command == "welcome":
      self.MAIN_SCRIPT(self, 1, command, self.welcome, x)
    elif command == "bio":
      self.MAIN_SCRIPT(self, 1, command, self.bio, x)
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
    self.git(self)
  
  def MAIN_SCRIPT(self, z: Optional[int], command, y, x: str): 
    print(f"{z}\n{command}\n{y}\n{x}")
    if z==0:
      self.FIND_COMMAND(self, command, y, x)
      return
    elif z==1:
      print(y[-1])
    elif z==2:
      print(y[-1])
    if z != 0 or z != None:
      return self.CHANGE_ARRAY(self, y, x)
