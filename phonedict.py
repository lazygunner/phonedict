import urllib2
import re
import sys
import getopt

def usage():
    print 'This tool is designed to generate a phone number dictionary.'
    print '============================================================'
    print 'Usage:'
    print '-p, --province: the province where the city in, default:zhejiang'
    print '-c, --city: the city where the number in, default:hangzhou'
    print '-f, --file: the output dictionary file, default:phone_dict.txt'
    print '-d: debug mode, show the generating messages'
    print 'example: python phonedict.py -p zhejiang -c hangzhou -f out.txt'
    print 'author:lazygunner, email:gymgunner@gmail.com'


def main(argv):
    city = 'hangzhou'
    province = 'zhejiang'
    out_file = 'phone_dict.txt'
    try:
        opts, args = getopt.getopt(argv, "hp:c:f:d", ["help", "province:", "city:", "file:"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == "-d":
            global _debug
            _debug = 1
        elif opt in ("-p", "--province"):
            province = arg    
        elif opt in ("-c", "--city"):
            city = arg    
        elif opt in ("-f", "--file"):
            out_file = arg    
    dict_gen(province, city, out_file)        

def dict_gen(province, city, out_file):
    if _debug:
        print province + ',' + city +',' + out_file + '\n'
    base_url = 'http://www.iluohe.com/city/'
    url = base_url + province + '/' + city +'/'
    try:
        response = urllib2.urlopen(url)
    except:
        print 'Net work error!Please check your network and the city name!'
        sys.exit(2)
    html = response.read()

    p = re.compile(r'>(\d{7})<')
    numbers = p.findall(html)
    count = len(numbers)
    if _debug:
        print 'total number areas:%d\n'%count
    if count == 0:
        print 'city name error!\n'
        sys.exit(2)
    output = open(out_file, 'w')
    if _debug:
        p = 0
    for n in numbers:
        n = n + '0000'
        if _debug:
            per = p / float(count)
            print 'phone number area:%s %.2f%%\r'%(n, per*100),
            p+=1

        aNum = long(n)
        tempdict = ''
        for i in range(0,10000):
            tempdict += str(aNum + i) + '\n'
        output.write(tempdict)
        output.flush()
    
    output.close()
    print 'phone number dictionary generated finished!'

if __name__ == '__main__':
    main(sys.argv[1:])

