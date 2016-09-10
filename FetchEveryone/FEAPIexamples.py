import FEobjAPI
import zlib
import urllib

testobj = FEobjAPI.objAPI()
testobj.loadToken()

print 'Running getResource test'
resdict = {'request':'forum/threads'}

testresult = testobj.getResource(resdict)
print testresult

for forumthread in testresult['response']:
    print 'Thread title:',forumthread['title'],'last post',forumthread['lastpost']

print 'Running putResource test'
resdict = {'request':'training/import'}

with open('example.tcx','r') as f:
    uzdata = urllib.quote_plus( zlib.compress(f.read()) )

datadict = {'uid':1684,'method':'TCX','category':'R','data':uzdata}

testresult = testobj.putResource(resdict,datadict)

print 'Server response:', testresult
