#!/usr/bin/python
#-*- coding: utf-8 -*-
import xbmc,xbmcaddon,xbmcgui,xbmcplugin
import base64,os,sys,time
import re,urllib,urllib2
AddonID='script.xvbmc.updatertools'
ADDON=xbmcaddon.Addon(id=AddonID)
addonInfo=xbmcaddon.Addon().getAddonInfo
dialog=xbmcgui.Dialog()
HOME=xbmc.translatePath('special://home/')
MainTitle="XvBMC Nederland"
waarschuwing='[COLOR=red][B]!!!  WARNING  !!![/B][/COLOR]'
readme='if you\'re seeing this message read this first[B]:[/B]'
noservicepack='Sorry the [B]S[/B]ervice[B]P[/B]ack update is [COLOR=red]outdated[/COLOR] at this moment'
notforked='[COLOR dimgray](the newest XvBMC\'s [B]Pi[/B]-image is not forked, [B]yet[/B]...)[/COLOR]'
subtitleNope="[COLOR=red][B]!!!  NOPE  !!![/B][/COLOR]"
nonlinux="[US] you\'re running a \'none linux os\' (Open-/LibreELEC)"
nonelecNL="[NL] dit is geen Raspberry Pi met Open-/LibreELEC \'OS\'"
base='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL3ppcHMv'
basewiz='aHR0cHM6Ly9hcmNoaXZlLm9yZy9kb3dubG9hZC94dmJtY3dpemFyZHov'
bldversietxt=xbmc.translatePath(os.path.join('special://home/userdata','versiebld.txt'))
bldversietxtwiz=xbmc.translatePath(os.path.join('special://home/userdata','wizbld.txt'))
repos='aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL1h2Qk1DL3JlcG9zaXRvcnkueHZibWMvbWFzdGVyL1JFUE9zaXRvcnkvemlwcy9yZXBvc2l0b3J5Lnh2Ym1jLw=='
EminenceTxt=xbmc.translatePath(os.path.join('special://home/userdata','eminence-sp.txt'))
EminenceUrl=base64.b64decode(basewiz)+'eminence-sp.txt'
NoxSpinTxt=xbmc.translatePath(os.path.join('special://home/userdata','noxspin-sp.txt'))
NoxSpinUrl=base64.b64decode(basewiz)+'noxspin-sp.txt'
PortableTxt=xbmc.translatePath(os.path.join('special://home/userdata','portable-sp.txt'))
PortableUrl=base64.b64decode(base)+'update/service/portable-sp.txt'
RPiTxt=xbmc.translatePath(os.path.join('special://home/userdata','rpi-sp.txt'))
RPiUrl=base64.b64decode(base)+'update/service/rpi-sp.txt'
ZeitgeistTxt=xbmc.translatePath(os.path.join('special://home/userdata','zeitgeist-sp.txt'))
ZeitgeistUrl=base64.b64decode(basewiz)+'zeitgeist-sp.txt'
EminenceTxtBld=xbmc.translatePath(os.path.join('special://home/userdata','eminence-bld.txt'))
EminenceUrlBld=base64.b64decode(basewiz)+'eminence-bld.txt'
NoxSpinTxtBld=xbmc.translatePath(os.path.join('special://home/userdata','noxspin-bld.txt'))
NoxSpinUrlBld=base64.b64decode(basewiz)+'noxspin-bld.txt'
PortableTxtBld=xbmc.translatePath(os.path.join('special://home/userdata','portable-bld.txt'))
PortableUrlBld=base64.b64decode(base)+'update/builds/portable-bld.txt'
RPiTxtBld=xbmc.translatePath(os.path.join('special://home/userdata','rpi-bld.txt'))
RPiUrlBld=base64.b64decode(base)+'update/builds/rpi-bld.txt'
ZeitgeistTxtBld=xbmc.translatePath(os.path.join('special://home/userdata','zeitgeist-bld.txt'))
ZeitgeistUrlBld=base64.b64decode(basewiz)+'zeitgeist-bld.txt'
def killKodi():
 myplatform=platform()
 log("XvBMC_Platform: "+str(myplatform))
 try:os._exit(1)
 except:pass
 if myplatform=='osx':
  log("############   try osx force close  #################")
  try:os.system('killall -9 XBMC')
  except:pass
  try:os.system('killall -9 Kodi')
  except:pass
  dialog.ok(waarschuwing,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')
  try:xbmc.executebuiltin("Reboot")
  except:pass
 elif myplatform=='linux':
  log("############   try linux force close  #################")
  try:os.system('killall XBMC')
  except:pass
  try:os.system('killall Kodi')
  except:pass
  try:os.system('killall -9 xbmc.bin')
  except:pass
  try:os.system('killall -9 kodi.bin')
  except:pass
  dialog.ok(waarschuwing,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','(trying \'reboot\' after OK, else pull power cable.)')
  try:xbmc.executebuiltin("Reboot")
  except:pass
 elif myplatform=='android':
  log("############   try android force close  #################")
  try:os.system('adb shell am force-stop com.jesusboxmedia')
  except:pass
  try:os.system('adb shell am force-stop com.perfectzoneproductions.jesusboxmedia')
  except:pass
  try:os.system('adb shell am force-stop com.semperpax.spmc')
  except:pass
  try:os.system('adb shell am force-stop com.semperpax.spmc16')
  except:pass
  try:os.system('adb shell am force-stop com.spmc')
  except:pass
  try:os.system('adb shell am force-stop com.spmc16')
  except:pass
  try:os.system('adb shell am force-stop org.kodi')
  except:pass
  try:os.system('adb shell am force-stop org.lodi.mobi')
  except:pass
  try:os.system('adb shell am force-stop org.xbmc')
  except:pass
  try:os.system('adb shell am force-stop org.xbmc.cemc')
  except:pass
  try:os.system('adb shell am force-stop org.xbmc.cemc_pro')
  except:pass
  try:os.system('adb shell am force-stop org.xbmc.kodi')
  except:pass
  try:os.system('adb shell am force-stop org.xbmc.xbmc')
  except:pass
  try:os.system('adb shell am force-stop uk.dbmc')
  except:pass
  try:os.system('adb shell am force-stop uk.droidbox.dbmc')
  except:pass
  try:os.system('adb shell kill com.perfectzoneproductions.jesusboxmedia')
  except:pass
  try:os.system('adb shell kill com.semperpax')
  except:pass
  try:os.system('adb shell kill com.semperpax.spmc16')
  except:pass
  try:os.system('adb shell kill org.kodi')
  except:pass
  try:os.system('adb shell kill org.lodi.mobi')
  except:pass
  try:os.system('adb shell kill org.xbmc')
  except:pass
  try:os.system('adb shell kill org.xbmc.cemc')
  except:pass
  try:os.system('adb shell kill org.xbmc.cemc_pro')
  except:pass
  try:os.system('adb shell kill org.xbmc.kodi')
  except:pass
  try:os.system('adb shell kill org.xbmc.xbmc')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.com.semperpax.spmc16());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.fire());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.fire.guru());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.fire.guruv());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.kodi());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.xbmc());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.xbmc.kodi());')
  except:pass
  try:os.system('Process.killProcess(android.os.Process.org.xbmc.xbmc());')
  except:pass
  dialog.ok(waarschuwing,'Your system has been detected as Android, you ','[COLOR=yellow][B]MUST[/COLOR][/B] force close XBMC/Kodi. [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Either close using Task Manager (If unsure pull the plug).')
  try:xbmc.executebuiltin("Reboot")
  except:pass
 elif myplatform=='windows':
  log("############   try windows force close  #################")
  try:
   os.system('@ECHO off')
   os.system('tskill XBMC.exe')
  except:pass
  try:
   os.system('@ECHO off')
   os.system('tskill Kodi.exe')
  except:pass
  try:
   os.system('@ECHO off')
   os.system('tskill SMC.exe')
  except:pass
  try:
   os.system('@ECHO off')
   os.system('TASKKILL /im Kodi.exe /f')
  except:pass
  try:
   os.system('@ECHO off')
   os.system('TASKKILL /im XBMC.exe /f')
  except:pass
  try:
   os.system('@ECHO off')
   os.system('TASKKILL /im XBMC.exe /f')
  except:pass
  dialog.ok(waarschuwing,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.','Use task manager and NOT ALT F4')
 else:
  log("############   try atv force close  #################")
  try:os.system('killall AppleTV')
  except:pass
  log("############   try raspbmc force close  #################")
  try:os.system('sudo initctl stop kodi')
  except:pass
  try:os.system('sudo initctl stop xbmc')
  except:pass
  dialog.ok(waarschuwing,'If you\'re seeing this message it means the force close','was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.','(trying \'reboot\' after OK, else pull power cable.)')
  try:xbmc.executebuiltin("Reboot")
  except:pass
def platform():
 if xbmc.getCondVisibility('system.platform.android'):return 'android'
 elif xbmc.getCondVisibility('system.platform.linux'):return 'linux'
 elif xbmc.getCondVisibility('system.platform.windows'):return 'windows'
 elif xbmc.getCondVisibility('system.platform.osx'):return 'osx'
 elif xbmc.getCondVisibility('system.platform.atv2'):return 'atv2'
 elif xbmc.getCondVisibility('system.platform.ios'):return 'ios'
def verifyplatform():
 myplatform=platform()
 log("XvBMC_Platform: "+str(myplatform))
 if myplatform=='osx':
  dialog.ok(waarschuwing,readme,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees for OSX [B];-p[/B]')
  log("=== OSX ===")
 elif myplatform=='linux':
  log("=== Download de laatste XvBMC (Open-/LibreELEC) ServicePack ===")
 elif myplatform=='android':
  dialog.ok('[COLOR=red][B]!!!  IMPORTANT  !!![/COLOR][/B]','[COLOR=lime]There\'s also a specific XvBMC\'s Android add-on update(r)[/COLOR]','...enkel voor specifieke bonus Android add-on updates...',noservicepack+' '+notforked)
  log("=== Android ===")
 elif myplatform=='windows':
  log("=== Download de laatste XvBMC (Windows) ServicePack ===")
 else:
  dialog.ok(waarschuwing,readme,'[COLOR=white]XvBMC[/COLOR]\'s Update(r) should work, [B]but[/B]...','NO! guarantees though [B];-p[/B]')
  log("=== ATV2/iOS/OSMC/Raspbmc/etc ===")
def KODIVERSION(url):
 xbmc_version=xbmc.getInfoLabel("System.BuildVersion")
 version=xbmc_version[:4]
 log("XvBMC_v"+version)
 dialog.ok(MainTitle,'Your Kodi Version : [COLOR lime][B]%s[/B][/COLOR]'%version)
def checkXvbmcVersie():
 if os.path.isfile(EminenceTxtBld):
  file=open(EminenceTxtBld,'r')
  EminenceVersie=file.read()
  file.close()
  return 'EminenceTxtBld','[COLOR gray]'+EminenceVersie+'[/COLOR]'
 elif os.path.isfile(NoxSpinTxtBld):
  file=open(NoxSpinTxtBld,'r')
  NoxSpinVersie=file.read()
  file.close()
  return 'NoxSpinTxtBld','[COLOR gray]'+NoxSpinVersie+'[/COLOR]'
 elif os.path.isfile(PortableTxtBld):
  file=open(PortableTxtBld,'r')
  PortableVersie=file.read()
  file.close()
  return 'PortableTxtBld','[COLOR gray]'+PortableVersie+'[/COLOR]'
 elif os.path.isfile(RPiTxtBld):
  file=open(RPiTxtBld,'r')
  RPiVersie=file.read()
  file.close()
  return 'RPiTxtBld','[COLOR gray]'+RPiVersie+'[/COLOR]'
 elif os.path.isfile(ZeitgeistTxtBld):
  file=open(ZeitgeistTxtBld,'r')
  ZeitgeistVersie=file.read()
  file.close()
  return 'ZeitgeistTxtBld','[COLOR gray]'+ZeitgeistVersie+'[/COLOR]'
 else:
  return 'unknown',''
def removefolder(map,exclude=None):
 for root,dirs,files in os.walk(map,topdown=False):
  for name in files:
   if(root.find(exclude)>0):
    continue
   try:os.remove(os.path.join(root,name))
   except:pass
  for name in dirs:
   if(name==exclude):
    continue
   try:os.rmdir(os.path.join(root,name))
   except:pass
def REMOVE_EMPTY_FOLDERS():
 log("########### Start Removing Empty Folders #########")
 empty_count=0
 used_count=0
 for curdir,subdirs,files in os.walk(HOME):
  if len(subdirs)==0 and len(files)==0:
   empty_count+=1
   os.rmdir(curdir)
   log("successfully removed: "+curdir)
  elif len(subdirs)>0 and len(files)>0:
   used_count+=1
def TextBoxes(announce):
 class TextBox():
  WINDOW=10147
  CONTROL_LABEL=1
  CONTROL_TEXTBOX=5
  def __init__(self,*args,**kwargs):
   xbmc.executebuiltin("ActivateWindow(%d)"%(self.WINDOW))
   self.win=xbmcgui.Window(self.WINDOW)
   xbmc.sleep(500)
   self.setControls()
  def setControls(self):
   self.win.getControl(self.CONTROL_LABEL).setLabel('XvBMC - View Log[B]:[/B]')
   try:f=open(announce);text=f.read()
   except:text=announce
   self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
   return
 TextBox()
 while xbmc.getCondVisibility('Window.IsVisible(10147)'):
  time.sleep(.5)
def TextBoxesPlain(heading,announce):
 class TextBox():
  WINDOW=10147
  CONTROL_LABEL=1
  CONTROL_TEXTBOX=5
  def __init__(self,*args,**kwargs):
   xbmc.executebuiltin("ActivateWindow(%d)"%(self.WINDOW))
   self.win=xbmcgui.Window(self.WINDOW)
   xbmc.sleep(500)
   self.setControls()
  def setControls(self):
   self.win.getControl(self.CONTROL_LABEL).setLabel(heading)
   try:f=open(announce);text=f.read()
   except:text=announce
   self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
   return
 TextBox()
 while xbmc.getCondVisibility('Window.IsVisible(10147)'):
  time.sleep(.5)
def facebook():
 TextBoxesPlain('XvBMC Nederland','[COLOR=red]NOTE:[/COLOR]\nXvBMC Nederland (xbmc nl) wij zijn geen helpdesk van/voor boxverkopers\n\nVoor meer informatie kijk op https://bit.ly/XvBMC-NL')
def AboutXvBMC():
 text=''
 twit='https://raw.githubusercontent.com/XvBMC/repository.xvbmc/master/readme.xml'
 req=urllib2.Request(twit)
 req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
 response=urllib2.urlopen(req)
 link=response.read()
 response.close()
 match=re.compile("<title>(.+?)</title><pubDate>(.+?)</pubDate>",re.DOTALL).findall(link)
 for status,dte in match:
  try:
   status=status.decode('ascii','ignore')
  except:
   status=status.decode('utf-8','ignore')
  dte=dte[:-15]
  status=status.replace('&amp;','')
  dte='[COLOR lime][B]'+dte+'[/B][/COLOR]'
  text=text+dte+'\n'+status+'\n'+'\n'
 infoTXT('[COLOR lime]Usage policy & Disclaimer [B]X[/B]v[B]BMC-[/B]NL[/COLOR]',text)
def infoTXT(heading,text):
 id=10147
 xbmc.executebuiltin('ActivateWindow(%d)'%id)
 xbmc.sleep(100)
 win=xbmcgui.Window(id)
 retry=50
 while(retry>0):
  try:
   xbmc.sleep(10)
   retry-=1
   win.getControl(1).setLabel(heading)
   win.getControl(5).setText(text)
   return
  except:
   pass
artwork=xbmc.translatePath(os.path.join('special://home','addons',AddonID,'/'))
fanart=artwork+'fanart.jpg'
def addonIcon():
 return artwork+'icon.png'
def message(text1,text2="",text3=""):
 if text3=="":
  xbmcgui.Dialog().ok(text1,text2)
 elif text2=="":
  xbmcgui.Dialog().ok("",text1)
 else:
  xbmcgui.Dialog().ok(text1,text2,text3)
def message_yes_no(text1,text2="",text3=""):
 if text3=="":yes_pressed=xbmcgui.Dialog().yesno(text1,text2)
 elif text2=="":yes_pressed=xbmcgui.Dialog().yesno("",text1)
 else:yes_pressed=xbmcgui.Dialog().yesno(text1,text2,text3)
 return yes_pressed
def infoDialog(message,heading=addonInfo('name'),icon=addonIcon(),time=3000):
 try:
  dialog.notification(heading,message,icon,time,sound=False)
 except:
  execute("Notification(%s,%s, %s, %s)"%(heading,message,time,icon))
def okDialog(line1,line2,line3,heading=addonInfo('name')):
 return dialog.ok(heading,line1,line2,line3)
def yesnoDialog(line1,line2,line3,heading=addonInfo('name'),nolabel='',yeslabel=''):
 return dialog.yesno(heading,line1,line2,line3,nolabel,yeslabel)
def log(msg,level=xbmc.LOGNOTICE):
 name='XvBMC_NOTICE'
 level=xbmc.LOGNOTICE
 try:
  xbmc.log('%s: %s'%(name,msg),level)
 except:
  try:
   xbmc.log('Logging Failure',level)
  except:
   pass
def forceRefresh(melding=None):
 xbmc.executebuiltin('UpdateLocalAddons()');log("XvBMC_UpdateLocalAddons()")
 time.sleep(0.5)
 xbmc.executebuiltin('UpdateAddonRepos()');log("XvBMC_UpdateAddonRepos()")
 time.sleep(0.5)
 if melding:
  dialog.ok(MainTitle,'Force Refresh Repos and Update LocalAddons')
  try:
   xbmc.executebuiltin('ReloadSkin()');log("XvBMC_ReloadSkin()")
  except:pass
  try:
   xbmc.executebuiltin('Container.Refresh');log("Container.Refresh")
  except:pass
def get_kversion():
 full_version_info=xbmc.getInfoLabel('System.BuildVersion')
 baseversion=full_version_info.split(".")
 intbase=int(baseversion[0])
 return intbase
def setView(content,viewType):
 if content:
  xbmcplugin.setContent(int(sys.argv[1]),content)
 if ADDON.getSetting('auto-view')=='true':
  xbmc.executebuiltin("Container.SetViewMode(%s)"%ADDON.getSetting(viewType))
def closeandexit():
 xbmc.executebuiltin('Action(back)')
"""
    IF you copy/paste 'script.xvbmc.updatertools' please keep the credits -2- XvBMC-NL, Thx.
"""