'''
Created on 5 mai 2015

@author: Jaay
'''

import dns.resolver
 
bls = [
"0spam.fusionzero.com",
"access.redhawk.org",
"all.rbl.jp",
"all.s5h.net",
"all.spamrats.com",
"aspews.ext.sorbs.net",
"b.barracudacentral.org",
"backscatter.spameatingmonkey.net",
"bb.barracudacentral.org",
"bl.blocklist.de",
"bl.drmx.org",
"bl.emailbasura.org",
"bl.konstant.no",
"bl.mailspike.net",
"bl.mav.com.br",
"bl.nosolicitado.org",
"bl.nszones.com",
"bl.scientificspam.net",
"bl.score.senderscore.com",
"bl.spamcannibal.org",
"bl.spamcop.net",
"bl.spameatingmonkey.net",
"bl.spamstinks.com",
"bl.suomispam.net",
"blacklist.woody.ch",
"block.dnsbl.sorbs.net",
"bsb.empty.us",
"bsb.spamlookup.net",
"cbl.abuseat.org",
"cbl.anti-spam.org.cn",
"cblless.anti-spam.org.cn",
"cblplus.anti-spam.org.cn",
"cdl.anti-spam.org.cn",
"cidr.bl.mcafee.com",
"combined.rbl.msrbl.net",
"db.wpbl.info",
"dnsbl-1.uceprotect.net",
"dnsbl-2.uceprotect.net",
"dnsbl-3.uceprotect.net",
"dnsbl.anticaptcha.net",
"dnsbl.aspnet.hu",
"dnsbl.cobion.com",
"dnsbl.dronebl.org",
"projecthoneypot.org",
"dnsbl.inps.de",
"dnsbl.justspam.org",
"dnsbl.kempt.net",
"dnsbl.net.ua",
"dnsbl.rv-soft.info",
"dnsbl.rymsho.ru",
"dnsbl.sorbs.net",
"dnsbl.spam-champuru.livedoor.com",
"dnsbl.tornevall.org",
"dnsbl.webequipped.com",
"dnsbl.zapbl.net",
"dnsrbl.swinog.ch",
"dul.dnsbl.sorbs.net",
"dul.pacifier.net",
"dul.ru",
"dyn.nszones.com",
"dyna.spamrats.com",
"escalations.dnsbl.sorbs.net",
"exitnodes.tor.dnsbl.sectoor.de",
"fnrbl.fast.net",
"forbidden.icm.edu.pl",
"hostkarma.junkemailfilter.com",
"http.dnsbl.sorbs.net",
"images.rbl.msrbl.net",
"intercept.datapacket.net",
"ipbl.zeustracker.abuse.ch",
"ips.backscatterer.org",
"ix.dnsbl.manitu.net",
"korea.services.net",
"l1.bbfh.ext.sorbs.net",
"l2.apews.org",
"l2.bbfh.ext.sorbs.net",
"l3.bbfh.ext.sorbs.net",
"l4.bbfh.ext.sorbs.net",
"list.bbfh.org",
"list.blogspambl.com",
"list.quorum.to",
"lookup.dnsbl.iip.lu",
"mail-abuse.blacklist.jippg.org",
"misc.dnsbl.sorbs.net",
"multi.surbl.org",
"netbl.spameatingmonkey.net",
"netblockbl.spamgrouper.com",
"netscan.rbl.blockedservers.com",
"new.spam.dnsbl.sorbs.net",
"noptr.spamrats.com",
"old.spam.dnsbl.sorbs.net",
"pbl.spamhaus.org",
"phishing.rbl.msrbl.net",
"pofon.foobar.hu",
"problems.dnsbl.sorbs.net",
"proxies.dnsbl.sorbs.net",
"psbl.surriel.com",
"rbl.abuse.ro",
"rbl.blockedservers.com",
"rbl.dns-servicios.com",
"rbl.efnet.org",
"rbl.efnetrbl.org",
"rbl.interserver.net",
"rbl.iprange.net",
"rbl.megarbl.net",
"rbl.polarcomm.net",
"rbl.rbldns.ru",
"rbl.talkactive.net",
"rbl2.triumf.ca",
"recent.spam.dnsbl.sorbs.net",
"relays.bl.kundenserver.de",
"relays.dnsbl.sorbs.net",
"rep.mailspike.net",
"safe.dnsbl.sorbs.net",
"sbl.nszones.com",
"sbl.spamhaus.org",
"singlebl.spamgrouper.com",
"short.rbl.jp",
"smtp.dnsbl.sorbs.net",
"socks.dnsbl.sorbs.net",
"spam.dnsbl.anonmails.de",
"spam.dnsbl.sorbs.net",
"spam.pedantic.org",
"spam.rbl.blockedservers.com",
"spam.rbl.msrbl.net",
"spam.spamrats.com",
"spamguard.leadmon.net",
"spamlist.or.kr",
"spamrbl.imp.ch",
"spamsources.fabel.dk",
"srn.surgate.net",
"st.technovision.dk",
"tor.dnsbl.sectoor.de",
"torexit.dan.me.uk",
"truncate.gbudb.net",
"ubl.unsubscore.com",
"virbl.dnsbl.bit.nl",
"virus.rbl.jp",
"virus.rbl.msrbl.net",
"vote.drbl.caravan.ru",
"vote.drbl.gremlin.ru",
"web.dnsbl.sorbs.net",
"web.rbl.msrbl.net",
"work.drbl.caravan.ru",
"work.drbl.gremlin.ru",
"wormrbl.imp.ch",
"xbl.spamhaus.org",
"z.mailspike.net",
"zen.spamhaus.org",
"zombie.dnsbl.sorbs.net",
"dnsbl.burnt-tech.com",
]
 
 
def checkDNSBL(server):
    for bl in bls:
        try:
            my_resolver = dns.resolver.Resolver()
            query = '.'.join(reversed(str(server).split("."))) + "." + bl
            answers = my_resolver.query(query, "A")
            answer_txt = my_resolver.query(query, "TXT")
            print 'IP: %s IS listed in %s (%s: %s)' %(server, bl, answers[0], answer_txt[0])
        except dns.resolver.NXDOMAIN:
            print 'IP: %s is NOT listed in %s' %(server, bl)
        except dns.resolver.NoAnswer:
            print 'No answer from %s' %(bl)

if __name__ == '__main__':
    checkDNSBL("212.83.179.87")

