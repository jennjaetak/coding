import re

class GCrossSearch:

    def split2words(self, keywordinfo, serial=None):
        split2wordslist = []
        for keyword in keywordinfo:
            dic8 = {'key': '', 'contentsType': keyword['contentsType']}
            dic8['key'] = re.split("\s+", keyword['keyword'])
            split2wordslist.append(dic8)
        return split2wordslist

    def sentence2word(self, sentenceinfo):
        wordlist = []
        for sentence in sentenceinfo:
            dic = {'sentenceSerial': sentence['sentenceSerial'], 'split': re.split("\s+", sentence['sentence'])}
            wordlist.append(dic)
        return wordlist

    def keywordsplit(self, sentenceinfo, keywordinfo):
        # wordlist = self.sentence2word(sentenceinfo) # 자소서 전체 쪼갬  ; 6 - '커튼콜', '일본어', '쓰기대회' ;  5 - '과목', '우수상'
        dlist = []
        clist = self.split2words(keywordinfo) # ['일본어', '쓰기대회']
        for cword in clist:
            nword = cword['key'][0]
            for idx in range(len(cword['key'])) :
                if idx > 0:
                    nword = nword + ' ' + cword['key'][idx]   # 커튼콜, 과목 우수상, 일본어 쓰기대회  # 여러 어절인 경우에 대해서 수정할 예정
            for set in sentenceinfo :
                if nword in set['sentence'] :
                    dic2 = {'key': nword, 'serial': set['sentenceSerial'], 'contentsType': cword['contentsType']}
                    if dic2 not in dlist:
                        dlist.append(dic2)
        return dlist

    def todict(self, sentenceinfo, keywordinfo):
        dlist = self.keywordsplit(sentenceinfo, keywordinfo)
        seriallist = []
        for d in dlist:
            dic3 = {'key': d['key'], 'serial': d['serial'], 'sentence': '', 'keypos': '', 'contentsType': d['contentsType']}
            for sentinfo in sentenceinfo:
                if d['serial'] == sentinfo['sentenceSerial']:
                    dic3['sentence'] = sentinfo['sentence']
                    dic3['keypos'] = sentinfo['sentence'].index(d['key'])
                    seriallist.append(dic3)
        return seriallist
