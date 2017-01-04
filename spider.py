import requests
import pyPdf
import os
keywords = 'is searchable'
# get the comment by id.
def getComment(id):
    url = "https://www.regulations.gov/dispatch/LoadDocumentDetail"
    data = '7|0|10|https://www.regulations.gov/Regs/|0EF855B0393EDDE0CF6CB49F76BDE4E0|com.gwtplatform.dispatch.rpc.shared.DispatchService|execute|java.lang.String/2004016611|com.gwtplatform.dispatch.rpc.shared.Action|6uLBCdyj2ElcnHkMBymQky7A|gov.egov.erule.regs.shared.action.LoadDocumentDetailAction/3833214929|d|EPA-HQ-OAR-2013-0602-' + str(id) +'|1|2|3|4|2|5|6|7|8|9|10|'
            # 7|0|10|https://www.regulations.gov/Regs/|0EF855B0393EDDE0CF6CB49F76BDE4E0|com.gwtplatform.dispatch.rpc.shared.DispatchService|execute|java.lang.String/2004016611|com.gwtplatform.dispatch.rpc.shared.Action|mSsGJB7f05jQkc4wKZ1eG9F8|gov.egov.erule.regs.shared.action.LoadDocumentDetailAction/3833214929|d|EPA-HQ-OAR-2013-0602-|1|2|3|4|2|5|6|7|8|9|10|
    headers = {
        'Host': 'www.regulations.gov',
        'Connection': 'keep-alive',
        'Content-Length': '352',
        'X-NewRelic-ID': 'UAQEUV5bGwcDU1NbDwM=',
        'Origin': 'https://www.regulations.gov',
        'X-GWT-Permutation': 'EBF873CB0BAA2FDE72FA95FA920A8DFE',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Content-Type': 'text/x-gwt-rpc; charset=UTF-8',
        'X-GWT-Module-Base': 'https://www.regulations.gov/Regs/',
        'Accept': '*/*',
        'Referer': 'https://www.regulations.gov/document?D=EPA-HQ-OAR-2013-0602-' + str(id),
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        'Cookie': 'fsr.r=%7B%22d%22%3A30%2C%22i%22%3A%22de358f9-93350593-6faf-4265-e6397%22%2C%22e%22%3A1484080517329%7D; fsr.s=%7B%22v2%22%3A-2%2C%22v1%22%3A1%2C%22cp%22%3A%7B%22cxreplayaws%22%3A%22true%22%7D%2C%22rid%22%3A%22de358f9-93350593-6faf-4265-e6397%22%2C%22to%22%3A4%2C%22c%22%3A%22https%3A%2F%2Fwww.regulations.gov%2Fdocument%22%2C%22pv%22%3A37%2C%22lc%22%3A%7B%22d0%22%3A%7B%22v%22%3A37%2C%22s%22%3Afalse%7D%7D%2C%22cd%22%3A0%2C%22sd%22%3A0%2C%22l%22%3A%22en%22%2C%22i%22%3A-1%7D; JSESSIONID=oKzC0nJUitpGxBq94x1CNffP; _gat_EPA=1; _gat_GSA=1; _ga=GA1.2.998353595.1483475349; _gat=1; _ceg.s=oj8gfi; _ceg.u=oj8gfi'
    }
    r = requests.post(url, data=data, headers=headers)
    s = r.text
    results = s.split(',[')[1].split('],')[0].split(',')
    print results
    foundIt = 'No'
    for result in results:
        if keywords in result:
            foundIt = 'Yes'
    print foundIt
# will pull the PDF file from api and save it in the current folder. Then convert it into text output. 
def getPDF(id):
    for num in range(1,3):
        print '=========================================================================='
        url = "https://www.regulations.gov/contentStreamer"
        params = {'documentId':'EPA-HQ-OAR-2013-0602-' + str(id), 'attachmentNumber': str(num), 'disposition': 'attachment', 'contentType':'pdf' }
        r = requests.get(url, params=params)
        name = str(id) + '_' + str(num) + '.pdf'
        with open(name, 'wb') as fd:
            for chunk in r.iter_content(2000):
                fd.write(chunk)
        try:
            pdf = pyPdf.PdfFileReader(open(name, "rb"))
            foundIt = 'No'
            for page in pdf.pages:
                print page.extractText()
                if keywords in page.extractText():
                    foundIt = 'Yes'
                    break
            print foundIt
        except:
            os.remove(name)

for i in range(28500, 28510):
	getComment(i)
	getPDF(i)

# getComment(28554)
# getPDF(28554)

