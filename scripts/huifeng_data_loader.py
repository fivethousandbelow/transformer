from datetime import datetime
import os
import sys

def get_data_days() :
    aa = ['20190102  20190130  20190306 20190403  20190507  20190605  20190704  20190801  20190829  20190927  20191101  20191129  20191227  20200205  20200304  20200402 20190103  20190131  20190307  20190404  20190508  20190606  20190705  20190802  20190830  20190930  20191104  20191202  20191230  20200206  20200305  20200403 20190104  20190201  20190308  20190408  20190509  20190610  20190708  20190805  20190902  20191008  20191105  20191203  20191231  20200207  20200306  20200407 20190107  20190211  20190311  20190409  20190510  20190611  20190709  20190806  20190903  20191009  20191106  20191204  20200102  20200210  20200309  20200408 '
'20190108  20190212  20190312  20190410  20190513  20190612  20190710  20190807  20190904  20191010  20191107  20191205  20200103  20200211  20200310  20200409 '
'20190109  20190213  20190313  20190411  20190514  20190613  20190711  20190808  20190905  20191011  20191108  20191206  20200106  20200212  20200311  20200410 '
'20190110  20190214  20190314  20190412  20190515  20190614  20190712  20190809  20190906  20191014  20191111  20191209  20200107  20200213  20200312  20200413 '
'20190111  20190215  20190315  20190415  20190516  20190617  20190715  20190812  20190909  20191015  20191112  20191210  20200108  20200214  20200313  20200414 '
'20190114  20190218  20190318  20190416  20190517  20190618  20190716  20190813  20190910  20191016  20191113  20191211  20200109  20200217  20200317  20200415 '
'20190115  20190219  20190319  20190417  20190521  20190619  20190717  20190814  20190911  20191017  20191114  20191212  20200110  20200218  20200318 '
'20190116  20190220  20190320  20190418  20190522  20190620  20190718  20190815  20190912  20191018  20191115  20191213  20200113  20200219  20200319 '
'20190117  20190221  20190321  20190419  20190523  20190621  20190719  20190816  20190916  20191021  20191118  20191216  20200114  20200220  20200320 '
'20190118  20190222  20190322  20190422  20190524  20190624  20190722  20190819  20190917  20191022  20191119  20191217  20200116  20200221  20200323 '
'20190121  20190225  20190325  20190423  20190527  20190625  20190723  20190820  20190918  20191023  20191120  20191218  20200117  20200224  20200324 '
'20190122  20190226  20190326  20190424  20190528  20190626  20190724  20190821  20190919  20191024  20191121  20191219  20200120  20200225  20200325 '
'20190123  20190227  20190327  20190425  20190529  20190627  20190725  20190822  20190920  20191025  20191122  20191220  20200121  20200226  20200326 '
'20190124  20190228  20190328  20190426  20190530  20190628  20190726  20190823  20190923  20191028  20191125  20191223  20200122  20200227  20200327 '
'20190125  20190301  20190329  20190429  20190531  20190701  20190729  20190826  20190924  20191029  20191126  20191224  20200123  20200228  20200330 '
'20190128  20190304  20190401  20190430  20190603  20190702  20190730  20190827  20190925  20191030  20191127  20191225  20200203  20200302  20200331 '
'20190129  20190305  20190402  20190506  20190604  20190703  20190731  20190828  20190926  20191031  20191128  20191226  20200204  20200303  20200401 ']
    dates = aa[0].split(' ')
    dates = [ datetime.strptime( x, '%Y%m%d') for x in list( filter( lambda x: x != '', dates ))]
    dates.sort()
    return dates 

def download_day( day ) :
    datestring = day.strftime('%Y%m%d')
    command='scp -r user1@172.37.44.98:/data/cffex/' + datestring + ' /Volumes/LaCie/china_market/cffex/'
    os.system(command)  
    print( 'processed ', day )

if __name__ == '__main__':
    data_days = get_data_days()
    if len(sys.argv)==3 :
        dd = sd = datetime.strptime( sys.argv[1], '%Y%m%d' )
        ed = datetime.strptime( sys.argv[2], '%Y%m%d' )
        while dd < ed + timedelta(days=1) : 
            if dd in data_days :
                download_day( day )
            else :
                print( dd, ' weekend or no data, skip' )
            dd = dd + timedelta(days=1)
    elif len(sys.argv) == 2 :
        dd = datetime.strptime( sys.argv[1], '%Y%m%d' )
        if dd in data_days :
            download_day( dd )
        else :
            print( dd, ' not exist in /data/cffex/, please check' )
    else :
        print( 'please enter one day or two days as arguments in format of YYYYMMDD' )
       
        