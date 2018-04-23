#coding=utf-8
import urllib2,sys,time,datetime,os,pymysql.cursors
from setting import headers, domain, start_url, file_output

read_file=open("readed.txt","a")
alldatas={}
readed_file = open("readed.txt","r")
for lines in readed_file:
        data = lines.strip("\n")
        alldatas[data]="readed"

connection = pymysql.connect(host='127.0.0.1', port=3306, user='test', password='test', db='cars', charset='gbk', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

 
for n in range(1,100):
    print n
    pageurl=start_url
    if n>1:
        pageurl="https://www.che168.com/suzhou/a0_0msdgscncgpi1ltocsp"+bytes(n)+"exy96x0/"

    try:
        carList=urllib2.urlopen(pageurl) 
    except Exception,e:
                print 'openERR:'
                print carList
                print str(e)
    else:
        if carList:
            carListPage=carList.read()
            if len(carListPage)<100 :
                os.system(r"rasphone -h 051213869974")  
                os.system(r"rasdial 051213869974 051213869974 085564") 
                os.system("run.bat")
                read_file.close()
                connection.close()
                sys.exit(9)

            carListPage=carListPage[carListPage.index("<div class=\"list-photo\">"):carListPage.index("<div class=\"page fn-clear\" id=\"listpagination\">")]
            carList=carListPage.split("<a target=\"_blank\" href=\"")
            carList.remove(carList[0])
            for car in carList:
                carList[carList.index(car)]=domain+car[:car.index("\"")]
            

            carsnum=len(carList)

            for i in range(0,carsnum):
                try:
                 
                    if carList[i] in alldatas :
                        pass
                        continue
                    try:
                        #urltmp = "https://www.che168.com/dealer/269052/24111384.html?pvareaid=100519"
                        #car=urllib2.urlopen(urltmp) 
                        car=urllib2.urlopen(carList[i]) 
                    except Exception,e:
                                print 'openERR:'
                                print carList[0]
                                print str(e)
                    else:
                        if car:
                            carPage=car.read()
                            data=carPage
                            if len(carPage)<100 :
                                os.system(r"rasphone -h 051213869974")  
                                os.system(r"rasdial 051213869974 051213869974 085564") 
                                os.system("run.bat")
                                read_file.close()
                                connection.close()      
                                sys.exit(9)
                            title=data[data.index("<h2>")+4:data.index("</h2>")]
                            che_yuan=""
                            if "personal" in carList[i]:
                                che_yuan="personal"
                            if "dealer" in carList[i]:
                                che_yuan="company"
                            if len(che_yuan)<3:
                                print "err at che yuan"
                                print carList[i]
                                pass
                                continue


                            shang_jia=""
                            shang_jia_dian_hua=""
                            shang_jia_zai_shou=""
                            shang_jia_yi_shou=""
                            shang_jia_lei_xin=""
                            shang_jia_di_zhi=""
                            price=data[data.index("<div class=\"car-price\">"):]
                            price1=price[price.index("<ins>")+5:price.index("</ins>")].strip(" ")
                            price2=price[price.index("<span class=\"unit\">")+19:price.index("</span>")].strip(" ")
                            price=price1+price2
                            print price
                            details=data[data.index("<div class=\"details\">")+21:]
                            details=details[:details.index("</div>")]
                            detailitems=details.split("<li>")
                            detailitems.remove(detailitems[0])
                            mils=detailitems[0].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>")
                            registered_year=detailitems[1].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>").split("-")[0]
                            registered_month=detailitems[1].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>").split("-")[1]
                            gear=detailitems[2].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>").strip("／")
                            displacement=detailitems[2].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>")
                            location=detailitems[3].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>") 
                            vehicle_emissions_standard=detailitems[4].split("</span>")[0].strip("<i>").strip("</i>").strip("<span>") 
                            infotext=data[data.index("<div class=\"content tab tab02\" id=\"anchor01\">"):]
                            infotext=infotext[:infotext.index("</ul>")]
                            infotext=infotext[infotext.index("<ul class=\"infotext-list fn-clear\">"):]
                            infotexts=infotext.split("</li>")
                            nian_jian= infotexts[0].split("</span>")[1].strip(" ").strip("&nbsp;")
                            bao_xian= infotexts[1].split("</span>")[1].strip(" ").strip("&nbsp;")
                            zhi_bao= infotexts[2].split("</span>")[1].strip(" ").strip("&nbsp;")
                            pai_fang= infotexts[3].split("</span>")[1].strip(" ").strip("&nbsp;")
                            guohu=""
                            if "</span>" in infotexts[4]:
                                if ">" in infotexts[4].split("</span>")[1]:
                                    guo_hu= infotexts[4].split("</span>")[1].split(">")[1].strip(" ")
                                else:
                                    guo_hu= infotexts[4].split("</span>")[1].strip(" ")
                                    print guo_hu
                            yong_tu= ""
                            wei_bao= ""
                            jian_jie=""
                            infotext2=data[data.index("<div class=\"content tab tab02\" id=\"anchor02\">"):]
                            infotext2=infotext2[:infotext2.index("</ul>")]
                            infotext2=infotext2[infotext2.index("<ul class=\"infotext-list fn-clear\">"):]
                            infotexts2=infotext2.split("</li>")              
                            fa_dong_ji= infotexts2[0].split("</span>")[1].strip(" ")
                            bian_su_qi= infotexts2[1].split("</span>")[1].strip(" ")
                            ji_bie= infotexts2[2].split("</span>")[1].strip(" ")
                            yan_se= infotexts2[3].split("</span>")[1].strip(" ")
                            ran_you= infotexts2[4].split("</span>")[1].strip(" ")
                            qu_dong= infotexts2[5].split("</span>")[1].strip(" ")
                            kou_bei= infotexts2[6].split("</span>")[1].split("</em>")[0].split(">")[1]
                            tu=""
                            id=  data[data.index("<link rel=\"canonical\" href=\""):]
                            id=id[id.index("href=\"")+6:id.index(">")]
                            id=id[:id.index("\"")]
                            if "dealer/" in id and "html" in id:
                                id=carList[i]
                                shang_jia=data[data.index("<div class=\"car-title\">"):]
                                
                                shang_jia=shang_jia[:shang_jia.index("<i class=\"iconfont drop-down\">")]
                                
                                shang_jia_di_zhi=data[data.index("<p class=\"address\">")+19:]
                                shang_jia_di_zhi=shang_jia_di_zhi[:shang_jia_di_zhi.index("</p>")]
                                shang_jia=shang_jia[shang_jia.index("</i>")+4:]
                                yong_tu= infotexts[5].split("</span>")[1].strip(" ")
                                wei_bao= infotexts[6].split("</span>")[1].strip(" ")
                            elif   "personal/" in id and "html" in id:
                                che_yuan="personal"   
                                id=carList[i]
                                #id=id[id.index("personal/"):id.index(".html")-1]
                                if "<div class=\"user-title\">" in data :
                                    shang_jia=data[data.index("<div class=\"user-title\">"):]
                                    shang_jia=shang_jia[:shang_jia.index("</div>")]
                                    if "</i>" in shang_jia:
                                        shang_jia=shang_jia[shang_jia.index("</i>")+4:]
                                else:
                                    shang_jia="personal"
                                yong_tu= infotexts[6].split("</span>")[1].strip(" ")
                                wei_bao= infotexts[7].split("</span>")[1].strip(" ")
                            else:
                                pass
                                continue
                            #id=pageurl
                            if len(id)<3:
                                pass
                                continue
                             
                            if "<" in shang_jia:
                                shang_jia=shang_jia[:shang_jia.index("<")]
                            shang_jia=shang_jia.strip("'").strip(" ").strip("\\").strip("@").strip("&")
                             
                            sqlValues="\'"+id+"\',\'"+che_yuan+"\',\'"+title+"\',\'"+price+"\',\'"+ mils+"\',\'"+registered_year+"\',\'"+ registered_month+"\',\'"+gear +"\',\'"+ displacement +"\',\'"+location+"\',\'"+ vehicle_emissions_standard+"\',\'"+nian_jian+"\',\'"+bao_xian +"\',\'"+ zhi_bao +"\',\'"+pai_fang+"\',\'"+ guo_hu+"\',\'"+yong_tu+"\',\'"+ wei_bao+"\',\'"+shang_jia +"\',\'"+jian_jie +"\',\'"+fa_dong_ji+"\',\'"+ bian_su_qi+"\',\'"+ji_bie+"\',\'"+ yan_se+"\',\'"+ran_you +"\',\'"+ qu_dong +"\',\'"+kou_bei+"\',\'"+ tu+"\',\'"+shang_jia_dian_hua+"\',\'"+ shang_jia_di_zhi+"\',\'"+shang_jia_zai_shou +"\',\'"+ shang_jia_yi_shou +"\',\'"+shang_jia_lei_xin+"\'"
                           
                            sql ="INSERT INTO `autohome` (`id`, `che_yuan`, `title`, `price`, `mils`, `registered_year`, `registered_month`, `gear`, `displacement`, `location`, `vehicle_emissions_standard`, `nian_jian`, `bao_xian`, `zhi_bao`, `pai_fang`, `guo_hu`, `yong_tu`, `wei_bao`, `shang_jia`, `jian_jie`, `fa_dong_ji`, `bian_su_qi`, `ji_bie`, `yan_se`, `ran_you`, `qu_dong`, `kou_bei`, `tu`, `shang_jia_dian_hua`, `shang_jia_di_zhi`, `shang_jia_zai_shou`, `shang_jia_yi_shou`, `shang_jia_lei_xin`) VALUES (" + sqlValues+ ")"
                            
                            try:
                                    cursor.execute(sql)
                                    connection.commit()
                                    print "sucess at:"+id
                            except Exception,e:
                                if "Duplicate" in str(e) or "PRIMARY" in str(e):
                                        print "try again"
                                        sql ="UPDATE  `autohome` SET `title`=\'"+title+"\',`che_yuan`=\'"+che_yuan+"\',  `price`=\'"+price+"\', `mils`=\'"+mils+"\', `registered_year`=\'"+registered_year+"\', `registered_month`=\'"+registered_month+"\', `gear`=\'"+gear+"\', `displacement`=\'"+displacement+"\', `location`=\'"+location+"\',  `vehicle_emissions_standard`=\'"+vehicle_emissions_standard+"\', `nian_jian`=\'"+nian_jian+"\', `bao_xian`=\'"+bao_xian+"\', `zhi_bao`=\'"+zhi_bao+"\', `pai_fang`=\'"+pai_fang+"\', `guo_hu`=\'"+guo_hu+"\',  `yong_tu`=\'"+yong_tu+"\', `wei_bao`=\'"+wei_bao+"\', `shang_jia`=\'"+shang_jia+"\', `jian_jie`=\'"+jian_jie+"\', `fa_dong_ji`=\'"+fa_dong_ji+"\', `bian_su_qi`=\'"+bian_su_qi+"\',  `ji_bie`=\'"+ji_bie+"\', `yan_se`=\'"+yan_se+"\', `ran_you`=\'"+ran_you+"\', `qu_dong`=\'"+qu_dong+"\', `kou_bei`=\'"+kou_bei+"\', `tu`=\'"+tu+"\',  `shang_jia_dian_hua`=\'"+shang_jia_dian_hua+"\', `shang_jia_di_zhi`=\'"+shang_jia_di_zhi+"\', `shang_jia_zai_shou`=\'"+shang_jia_zai_shou+"\', `shang_jia_yi_shou`=\'"+shang_jia_yi_shou+"\', `shang_jia_lei_xin`=\'"+shang_jia_lei_xin+"\' WHERE (`id`=\'"+id+"\')"
                                        try:
                                                #print "try update"
                                                cursor.execute(sql)
                                                connection.commit()
                                                #print "UPDATED DATA:"+id
                                               # print "update sucess"
                                                try:
                                                    alldatas[carList[i]]="readed"
                                                    read_file.write(carList[i]+"\n")
                                                    read_file.flush()      
                                                except Exception,e:
                                                    print "save err"
                                                    print str(e)
                                                    pass
                                                    continue    
                                        except Exception,e:
                                                print "update fauild"
                                                print str(e)
                                                pass
                                                continue
                                else:
                                        print "sql err"
                                        print str(e)
                                        pass
                                        continue
                            try:
                                alldatas[carList[i]]="readed"
                                read_file.write(carList[i]+"\n")
                                read_file.flush()    
                            except Exception,e:
                                print "save err"
                                print str(e)
                                pass
                                continue
                except Exception,e:
                    print "err"
                    print str(e)
                    pass
                    continue
                                        
                
            try:
                alldatas[pageurl]="readed"
                read_file.write(pageurl+"\n")
                read_file.flush()    
                print len(alldatas)
            except Exception,e:
                    
                print "save err"
                print str(e)
                pass
                continue   
read_file.close()
connection.close()     


        