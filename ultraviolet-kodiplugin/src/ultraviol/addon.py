import xbmcaddon
import xbmcgui
import ultraviol.spectrum.PlatformProviderSpectrum as pps

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1= "Hellow World"
line2=  " some text"
line3   = " Using python"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)


platformProvider = pps.PlatformProviderSpectrum()
