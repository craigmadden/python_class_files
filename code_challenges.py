# def hello_name(name):
#     print "Hello " + name + "!"
#
# hello_name("Bob")

from string import maketrans
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab,outtab)
str = "Yms bgb gr! Cmlepyrsjyrgmlq! Dgb wms sqc qrpgle.kyicrpylq? Id wms bgbl'r wms qfmsjb npmzyzjw em afcai gr msr. Ir kyicq rfgq ksaf cyqgcp."

print str.translate(trantab)