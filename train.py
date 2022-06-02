
"""




<center><h1>GÜNEŞ ENERJİSİ İLE ELEKTRİK ÜRETİM ANALİZİ</h1><hr></center>





<br>
<p>
<strong><center>Güneş Enerjisi Nedir?</strong><br><br>
Güneş enerjisi, kaynağı Güneş olan ısı ve parlak ışıktır. Güneş'in çekirdeğinde yer alan füzyon süreci ile açığa çıkan ışınım enerjisidir. Güneşteki hidrojen gazının helyuma dönüşmesi füzyon sürecinden kaynaklanır. Dünya atmosferinin dışında Güneş ışınımının şiddeti, aşağı yukarı sabit ve 1370 W/m2 (Watt/metrekare) değerindedir; ancak yeryüzünde 0-1100 W/m2 değerleri arasında değişim gösterir. Bu enerjinin Dünya'ya gelen küçük bir bölümü dahi,insanlığın mevcut enerji tüketiminden kat kat fazladır. Güneş enerjisinden yararlanma konusundaki çalışmalar özellikle 1970'lerden sonra hız kazanmış, Güneş enerjisi sistemleri teknolojik olarak ilerleme ve maliyet bakımından düşme göstermiş, Güneş enerjisi çevresel olarak temiz bir birincil enerji kaynağı olarak kendini kabul ettirmiştir.
</p><br>
<center><img src="https://seyler.ekstat.com/img/max/800/b/bIebrK8HYEF8xIVM-636996523804646072.jpg", width='500px'></center>
<br>

<p>
<strong><center>Neden Güneş Enerjisi?</strong><br><br>
Günden güne gelişen dünyamızda en önemli sorunlardan biride enerji ihtiyacıdır. Bu ihtiyaç yüzde 81 oranıyla fosil kaynaklarıyla karşılanır. Kısa zamanda bu kadar yoğun kullanılan fosil kaynaklı yakıtların çevreye olan zararı hakkında yapabileceğimiz hareketler pek de mümkün görünmüyor, ama bu yapabileceğimiz hiç bir şey yok anlamına gelmiyor. Bu, daha istikrarlı, sürdürülebilir ve çevreye zarar vermeyecek bir enerji kaynağı olan güneş enerjisinin önem kazanmasında rol oynamıştır.

<center>Bilindiği gibi dünyanın en büyük enerji kaynağı güneştir. Bitkiler güneş enerjisini kullanarak fotosentez yaparlar ve bunun sonucunda besin üretirler. Üretilen bu besin dünyadaki tüm canlıların gıda ihtiyacını karşılar. Güneş Enerjisinin bir etkisi de Dünyamızı ısıtmaktır. Gece olduğunda havanın soğumasından da anlayabileceğimiz gibi güneş yeryüzünün sıcaklığını arttırmaktadır. Bunun yanında deniz seviyesinde ulaşılabilen en yüksek Güneş enerjisi 1,020 W/m2’dir. Fakat bunun 3 ila 9 kWh/ m2 arasında değişen miktar kadarı elektriğe çevrilebiliyor.Güneş enerjisi temiz bir kaynaktır. Günümüzde dünyadaki en önemli çevre sorunlarından biri olan atmosferdeki karbondioksit oranının artışından ve sera etkisinden kaynaklanan küresel ısınmadır.
</p><br>
<center><img src="https://cw-enerji.com/wp-content/uploads/2020/03/1-2-1400x788-1-657x370.jpg", width='500px'>
<br><small>Erzincan Şehrindeki Güneş Enerjisi Santrali</small></center>
<p><br>
<center>Güneş Enerjisi;<br>
•Tükenmeyen ve temiz enerji kaynağıdır.<br>
•Bol miktarda bulunur.<br>
•Dışa bağımlılığı yoktur.<br>
•Kurulum maliyeti hariç ucuz bir kaynaktır.<br>
•Nakliye problemi yoktur.<br>
Böylelikle Güneş Enerjisi sürdürülebilir bir özelliğe sahiptir. Elektrik kullanımın olduğu her alanda güneş enerjisi kullanılabilir.<br>
</p><br>
<hr>
<p><br><strong><center>Bu Analizdeki Hedefimiz</strong><br>
      Kanada'da Calgary şehrinde bulunan 'Southland Leisure Centre' adlı eğlence merkezine ait güneş enerjisi ile elektrik üretimi verilerini ve şehire ait hava durumu verilerini de analiz ederek güneş santralindeki elektrik üretimine etki eden faktöreleri bulmayı ve bir sonraki gün de veya saatte üretilecek güneş enerjisini(kWh) tahmin etmeyi hedefliyoruz.<br>
      Bu doğrultuda <a href='https://data.calgary.ca/Environment/Solar-Energy-Production/ytdn-2qsp/data' target="_blank">Calgary</a>'den almış olduğumuz Southland Leisure Centre'a ait 2015 Eylül ayından başlayarak günümüze kadar olan her saat dilimine ait güneş enerjisi üretimi verilerini ve <a href='http://agriculture.alberta.ca/acis/weather-data-viewer.jsp' target="_blank">Alberta</a>'dan aldığımız Calgary şehrine ait olan hava durumu verilerini de kullanarak analizimizi gerçekleştireceğiz.
</p><br>

#Üretilen Elektrik Verilerini Okuma ve Temizleme
"""

# -*- coding: utf-8 -*-

import pandas as pd #Gerekli kutuphaneyi ekleme
#Pandas kutuphanesini veri okuma ve veriyi temizlemede kullanacagiz

df = pd.read_csv('https://raw.githubusercontent.com/kynemre/GunesEnerjisiVeriAnalizi/master/Solar_Energy_Production.csv')#Veri setini okuduk
df #Data'mizi goruntuluyoruz

"""<h3>Veri Setinin İçeriği</h3>
<p>Okuduğumuz veri setine baktığımızda, sütunlarda sırasıyla, santralin ismi, ID numarası, adresi, tarihi ve üretilen elektrik miktarı görünmektedir. Veriler günün 6 ile 21 saatleri arasında, saatlik olacak şekilde girilmiş.</p>
<p>Veri setinde birden fazla santral için veri girişi yapılmış. Analizin devamında, tek bir santral üzerinden gideceğiz.</p>
"""

#Veri setimizde birden fazla elektrik santrali var
data = df[df['address']=='2000 SOUTHLAND DR SW']#Sadece bir tane elektrik santralini isleyecegiz
data['date'] = data['date'].astype('datetime64')#Tarihleri zaman objesine cevirdik

data.isnull().any()#NaN degerleri kontrol ediyoruz
#Herhangi bir sutunda NaN deger yoktur

"""#Hava Durumu Verilerini Okuma ve Temizleme"""

data_weather = pd.read_csv('https://raw.githubusercontent.com/kynemre/GunesEnerjisiVeriAnalizi/master/HavaDurumuVeri.csv', encoding= 'unicode_escape')#Hava durumu verisini okuduk
data_weather

"""<h3>Veri Setinin İçeriği</h3>
<p>Veri setimiz, Ocak 2019 ve Mayıs 2020 tarihleri arasındaki, 17 hava durumu özniteliğini içeriyor. Hava durumu verileri, elektrik üretim verileri gibi saatlik olarak girilmiş.</p>
 <p>Bu verilerilerin kaynağı olan hava durumu istasyonu, güneş santralleri ile aynı bölgede bulunmaktadır.</p>
"""

data_weather.drop('Fusarium Severity Value',axis=1, inplace=True)
data_weather['Date (Local Standard Time)'] = data_weather['Date (Local Standard Time)'].astype('datetime64')
data_weather = data_weather.sort_values('Date (Local Standard Time)')#Verileri tarihe gore siraladik

data = data[(data['date'].apply(lambda x:x.hour)>=6) & 
                            (data['date'].apply(lambda x:x.hour)<=21) &
                            (data['date'] >= data_weather['Date (Local Standard Time)'].min()) &
                            (data['date'] <= data_weather['Date (Local Standard Time)'].max())] #Elektrik uretimi veri setinde gece icin girilen bilgiler var ise onlari sildik
data = data.sort_values('date')#Verileri tarihe gore siraladik

kontroller = list() #Icinde True/False tutacak olan bir liste olusturduk
for zaman in data['date'].values:#Hava durumunun tarihlerini saymaya basladik
  if zaman in data_weather['Date (Local Standard Time)'].values:#Hava durumunun tarihi, elektrik uretimi tarihleri icinde varsa True ekler
    kontroller.append(True)
  else:#Ayni tarihler yoksa False ekler
    kontroller.append(False)
data = data[kontroller]

#Bu kod blogunda iki ayri veri setinden okudugumuz verileri tek bir tabloda birlestirecegiz
#Verilerin dogru eslesebilmesi icin tarihleri kontrol edecegiz
kontroller = list()#Icinde True/False tutacak olan bir liste olusturduk
for zaman in data_weather['Date (Local Standard Time)'].values:#Hava durumunun tarihlerini saymaya basladik
  if zaman in data['date'].values:#Hava durumunun tarihi, elektrik uretimi tarihleri icinde varsa True ekler
    kontroller.append(True)
  else:#Ayni tarihler yoksa False ekler
    kontroller.append(False)

columns = data_weather.columns[2:].tolist()
for col in columns:
  data[col] = data_weather[kontroller][col].tolist()

data

"""#Verinin Görselleştirilmesi"""

import matplotlib.pyplot as plt
import seaborn as sns#Gerekli kutuphaneleri ekledik
#Kütüphaneleri, elimizdeki veriyi gorsellestirmek ve aralarindaki baglantiyi gormek icin kullanacagiz
import numpy as np

"""<h1>Elektrik Üretimi Grafiği</h1><br> Grafiğin x ekseni gün ay ve yıl olarak tarihleri belirtmektedir.<br> Grafiğin y ekseni elektrik üretim miktarını kWh cinsinden göstermektedir.<br>
1 Ocak 2019-5 Şubat 2019 tarihleri arası elektrik üretimi en çok 70 kWh'e çıkmaktadır.<br>5 Şubat 2019-12 Mart 2019 arası neredeyse 0 dır <br> En yoğun elektrik üretimi 12 Mart 2019 ile 12 Kasım 2019 arasında olmuştur.<br> 12 Kasım 2019'dan sonra elektrik üretim miktarı azalmaya başlamıştır ve bu azalma 20 Ocak 2020' ye kadar devam etmektedir.<br> 20 Ocak 2020'den itibaren elektrik üretiminde aralıklı ama hızlı bir artış olmuştur.



"""

plt.figure(figsize=(20,7))#Grafigimizi tanimladik
plt.plot(data['date'], data['kWh'], label='Uretilen Elektrik Miktari')#Grafigimizi cizdirdik

plt.xticks(np.linspace(data['date'].min().value, 
                       data['date'].max().value, 15).astype('datetime64[ns]'),
                       pd.to_datetime(np.linspace(data['date'].min().value, 
                       data['date'].max().value, 15)).strftime('%d %B %Y'), rotation=45)
plt.rc(['xtick','ytick'], labelsize=14)#x ve y eksen degerlerinin boyutlarini degistirdik

plt.title("Elektrik Uretimi", fontsize=17)#Grafige baslik ekledik
plt.ylabel('Uretim Miktari (kWh)', fontsize=15)#Grafigin y eksenine isim verdik
plt.xlabel('Tarih', fontsize=15)#Grafigin x eksenine isim verdik
plt.grid(axis='y', color='gray', linestyle='-', linewidth=0.5)#Grafige izgara ekledik
plt.legend(fontsize=13)#Grafik bilgilerini yazdirdik

plt.figure(figsize=(20,7))
plt.plot(data['date'], data['Air Temp. Inst. (°C)'], c='orange')

plt.xticks(np.linspace(data['date'].min().value, 
                       data['date'].max().value, 15).astype('datetime64[ns]'),
                       pd.to_datetime(np.linspace(data['date'].min().value, 
                       data['date'].max().value, 15)).strftime('%d %B %Y'), rotation=45)
plt.rc(['xtick','ytick'], labelsize=14)#x ve y eksen degerlerinin boyutlarini degistirdik

plt.title("Sıcaklık", fontsize=17)#Grafige baslik ekledik
plt.ylabel('Sıcaklık (°C)', fontsize=15)#Grafigin y eksenine isim verdik
plt.xlabel('Tarih', fontsize=15)#Grafigin x eksenine isim verdik
plt.grid(axis='y', color='gray', linestyle='-', linewidth=0.5)#Grafige izgara ekledik

"""<h1>Sıcaklık Grafiği</h1><br> Grafiğin x ekseni gün ay ve yıl olarak tarihleri belirtmektedir.<br> Grafiğin y ekseni sıcaklığı derece cinsinden göstermektedir.<br>1 Ocak 2019 ile 5 Şubat 2019 arasında -19 derece ile 28 dereceye kadar sapma olduktan sonra -20 ile 10 derece arasından yoğunlaşma olmuştur.<br>Grafikte en büyük sapma 5 Şubat 2019 ile 12 Mart 2019 arasında olmaktadır.<br>12 Mart 219 ile 8 Ekim 2019'a kadar sıcaklık değerlerinde genellikle 0 ve 20 derece arasında bir yoğunlaşma olmuştur. <br> 8 EKim 2019'dan sonra değerler dağınıktır ama genelde -20 ile 10 derece arasında kalmaktadır (16 Aralık 2019- 20 Ocak 2020 arası hariç= burada değerler yaklaşık -36 ya kadar düşmektedir ( Bu aralıktaki en büyük sapma budur.) .)

"""

gun = '2020-04-15 08:00:00'#Bir gun limiti belirliyoruz

#Normaliz edecegimiz kisimlari aliyoruz
#Normalize ediyoruz
uretim_norm = data[data['date'] >= gun]['kWh']
uretim_norm = uretim_norm/uretim_norm.max()

sicaklik_norm = data[data['date'] >= gun]['Air Temp. Inst. (°C)']
sicaklik_norm = sicaklik_norm-sicaklik_norm.min()
sicaklik_norm = sicaklik_norm/sicaklik_norm.max()

nem_norm = data[data['date'] >= gun]['Humidity Avg. (%)']
nem_norm = nem_norm-nem_norm.min()
nem_norm = nem_norm/nem_norm.max()

tarihler = data[data['date'] >= gun]['date']

plt.figure(figsize=(20,7))#Grafigi tanimladik
plt.bar(tarihler, uretim_norm, color='skyblue', label='Elektrik Üretimi')#Grafikleri cizdiriyoruz
plt.plot(tarihler, sicaklik_norm, color='orange', label='Sıcaklık')
plt.plot(tarihler, nem_norm, color='blue', label='Nem')

plt.xticks(np.linspace(tarihler.min().value, 
                       tarihler.max().value, 15).astype('datetime64[ns]'),
                       pd.to_datetime(np.linspace(tarihler.min().value, 
                       tarihler.max().value, 15)).strftime('%d %B %Y'), rotation=45)

plt.title('Üretilik eksenlerine isim veriyoruz
plt.ylabel('Normalize Edilmiş Değerler', fontsize=15en Elektrik, Sıcaklık ve Nem Oranı', fontsize=17)#Grafige baslik ekliyoruz
plt.xlabel('Tarih', fontsize=15)#Graf)

plt.grid(axis='y')#Grafige izgara ekliyoruz
plt.legend(loc=2, fontsize=13)#Grafik bilgilerini yazdiriyoruz

"""<h1>Üretilen Elektrik,Sıcaklık,Nem Oranı Grafiği</h1><br>Grafikte x ekseni tarihi vermektedir.<br> Grafikte y ekseni normalize edilmiş değerleri vermektedir.<br> Turuncu=sıcaklık, koyu mavi=nem, açık mavi= elektrik üretimini gösterir.<br> Grafikte en çok elektrik üretim yoğunluğu 19 Nisan 2020 ile 30 Nisan 2020 arasında olmuştur.<br> Elektrik üretiminin çok olduğu tarihlerde nem ve sıcaklık genellikle (yaklaşık olarak) eş zıt olarak görülmektedir."""

#Sadece ogle saatlerinden olusan bir veri olsuturduk
data_ogle = data[(data['date'].apply(lambda x:x.hour)>=12) & 
                            (data['date'].apply(lambda x:x.hour)<=16)]

sns.relplot(x = 'Air Temp. Inst. (°C)', y = 'kWh', data = data_ogle,
            size_order=["T1", "T2"],aspect=1, facet_kws=dict(sharex=False),
            kind="line", legend="full").fig.set_size_inches(20,7)#Grafigi cizdirdik

plt.title('Sıcaklığa Göre Elektrik Üretimi', fontsize=17)#Grafige baslik ekledik
plt.xlabel('Sıcaklık (°C)', fontsize=15)#Grafik eksenlerine isim verdik
plt.ylabel('Elektrik Üretimi (kWh)', fontsize=15)

plt.legend(loc=2, fontsize=13)#Grafik bilgilerini yazdirdik

"""<h1> Sıcaklığa Göre Elektrik Üretimi Grafiği </h1><br> Grafikte x ekseni sıcaklığı derece cinsinden göstermektedir.<br> Grafikte y ekseni elektrik üretimini kWh cinsinden göstermektedir.<br>-30 ve -10 derece arası elektrik üretiminde dalgalanmalara sebep olmuştur. Hem 0 kWh hem de 120 kWh görülmüştür bu aralıkta.Düzenli elektrik üretimi için uygun sıcaklık aralığı değildir.<br> -10 derece ile (yaklaşık)28 derece arası çok yüksek kWh elektrik üreilmese de yoğunluklu ve düzenli olarak elektrik üretimi olmuştur.<br> 28 derece(yaklaşık olarak) ve sonrası da elektrik üretimi için uygun bir sıcaklık değildir iniş ve çıkışlar çoktur."""

sns.relplot(x = 'Humidity Inst. (%)', y = 'kWh', data = data_ogle,
            size_order=["T1", "T2"],aspect=1, facet_kws=dict(sharex=False),
            kind="line", legend="full").fig.set_size_inches(20,7)#Grafigi cizdirdik

plt.title('Nem Oranına Göre Elektrik Üretimi', fontsize=17)#Grafige baslik ekledik
plt.xlabel('Nem Oranı (%)', fontsize=15)#Grafik eksen bilgilerini ekledik
plt.ylabel('Elektrik Üretimi (kWh)', fontsize=15)

plt.legend(loc=2, fontsize=13)#Grafik bilgilerini yazdirdik

"""<h1> Nem Oranına Göre Elektrik Üretimi</h1><br> Grafikte x ekseni nem oranını % cinsinden vermektedir.<br> Grafikte y ekseni elektrik üretimini kWh cinsinden göstermektedir.<br> Nem  oranı 0-%20 arası ani bir sapma dışında genellikle elektrik üretimi yüksektir. <br>Nem oranı yüzdelik olarak %20-%60 arasında iken sapmalar çok büyüktür 0-120 kWh arası ani inişler ve çıkışlar vardır.<br> Nem oranı %60-%93 arası sapmalar azdır  yoğunlaşmalar olmuştur.<br> (yaklaşık)%93'ten fazla olduğu zamanlar elektrik üretiminde ciddi düşüş görülmektedir."""

corr = data.corr()#Sutunlar arasindaki bagintiyi kurduk
plt.figure(figsize=(12,10))#Grafigi tanimladik
ax = sns.heatmap(
    corr, 
    cmap=sns.diverging_palette(140, 300, n=500),
    vmin=-1, vmax=1, center=0,
    square=True
)#Grafigi cizdirdik
ax.set_xticklabels(ax.get_xticklabels(), fontsize=12,rotation=45,horizontalalignment='right')
ax.set_yticklabels(ax.get_yticklabels(), fontsize=12)

gun = '2020-04-15 08:00:00'#Bir gun limiti belirliyoruz

#Normaliz edecegimiz kisimlari aliyoruz
#Normalize ediyoruz
uretim_norm = data[data['date'] >= gun]['kWh']
uretim_norm = uretim_norm/uretim_norm.max()

isinim_norm = data[data['date'] >= gun]['Incoming Solar Rad. (W/m2)']
isinim_norm = isinim_norm-isinim_norm.min()
isinim_norm = isinim_norm/isinim_norm.max()

tarihler = data[data['date'] >= gun]['date']

plt.figure(figsize=(20,7))#Grafigi tanimladik
plt.bar(tarihler, uretim_norm, color='skyblue', label='Elektrik Üretimi')#Grafikleri cizdiriyoruz
plt.plot(tarihler, isinim_norm, color='orange', label='Gelen Güneş Işınımı')

plt.xticks(np.linspace(tarihler.min().value, 
                       tarihler.max().value, 15).astype('datetime64[ns]'),
                       pd.to_datetime(np.linspace(tarihler.min().value, 
                       tarihler.max().value, 15)).strftime('%d %B %Y'), rotation=45)

plt.title('Gelen Güneş Işınımı ve Üretilen Elektrik', fontsize=17)#Grafige baslik ekliyoruz
plt.xlabel('Tarih', fontsize=15)#Grafik eksenlerine isim veriyoruz
plt.ylabel('Normalize Edilmiş Değerler', fontsize=15)

plt.grid(axis='y')#Grafige izgara ekliyoruz
plt.legend(loc=2, fontsize=13)#Grafik bilgilerini yazdiriyoruz

"""<h1> Gelen Güneş Işınımı ve Üretilen Elektrik Grafiği </h1><br> Grafikte x ekseni tarihleri göstermektedir.<br> Grafikte y ekseni normalize edilmiş değerleri göstermektedir.<br> Sarı= Gelen güneş ışınımı , Mavi=Elektrik üretimi <br> Grafikte genellikle gelen güneş ışınımı ile elektrik üretimi doğru orantılı olarak gitmektedir.<br> 30 Nisan 2020 ile 3 Mayıs 2020 arası doğru orantıya uymamaktadır."""

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

nitelikler = ['Air Temp. Inst. (°C)','Humidity Inst. (%)','Incoming Solar Rad. (W/m2)',
              'Wind Chill (°C)','Wind Speed 2 m Avg. (km/h)']#Tahmin icin referans alacagimiz verileri aldik

lr = LinearRegression()#Dogrusal tahmin icin objemizi olusturduk

y = data['kWh']#Ulasmak istedigimiz kume
x = data[nitelikler]#kullanacagimiz nitelikler
lr.fit(x,y)#Nitelikler ve sonuc arasindaki baglantiyi kurma

tahmin = lr.predict(x)#modellemeden tahmin yapma

ax1 = sns.distplot(y,hist=False,color='r',label='Gerçek değer')
sns.distplot(y_kestirilen,hist=False,color='b',label='Kestirilen değer',ax=ax1)

atlama_miktarı = 50 #Grafige cizilecek ornekleri azaltma

plt.figure(figsize=(20,8))
plt.plot(data['date'][::atlama_miktarı], y[::atlama_miktarı], c='red', label='Üretilen Elektrik')
plt.plot(data['date'][::atlama_miktarı], tahmin[::atlama_miktarı], linestyle='-.', c='blue', label='Tahmini Üretim')

plt.xlabel('Tarih', fontsize=15)
plt.ylabel('Üretim (kWh)', fontsize=15)
plt.title("Üretilen Elektrik ve Tahmin", fontsize=17)

plt.grid(linestyle='dashed' ,color='gray', linewidth=0.5)
plt.legend(fontsize=15)

#House-power vs price ilişkisini tekrar modelleyelim
y = data['kWh']#hedef, series
X = data[nitelikler]#kullanılacak özellikler, dataFrame 

lr = LinearRegression()
poly = PolynomialFeatures(degree=8)

egitim_poly = poly.fit_transform(X)
lr.fit(egitim_poly, y)
tahmin = lr.predict(egitim_poly)

tahmin = pd.DataFrame(tahmin, columns=['tahmin'])
tahmin[tahmin.tahmin <0] = 0
tahmin = tahmin['tahmin'].tolist()

#Gerçek ve kestirilen değerlerin dağılımlarının çizimi
ax1 = sns.distplot(data['kWh'],hist=False,color='r',label='Gerçek değer')
sns.distplot(tahmin,hist=False,color='b',label='Kestirilen değer',ax=ax1)

plt.figure(figsize=(20,8))
plt.plot(data['date'][::atlama_miktarı], y[::atlama_miktarı], c='red', label='Üretilen Elektrik')
plt.plot(data['date'][::atlama_miktarı], tahmin[::atlama_miktarı], linestyle='-', c='blue', label='Tahmini Üretim')

plt.xlabel('Tarih', fontsize=15)
plt.ylabel('Üretim (kWh)', fontsize=15)
plt.title("Üretilen Elektrik ve Tahmin", fontsize=17)

plt.grid(linestyle='dashed' ,color='gray', linewidth=0.5)
plt.legend(fontsize=15)

lr.predict(poly.fit_transform([[0, 57.3, 251.5, -2.7,20]]))

tahmin = lr.predict(poly.fit_transform(x[::200]))
tahmin = pd.DataFrame(tahmin, columns=['tahmin'])
tahmin[tahmin.tahmin <0] = 0
tahmin = tahmin['tahmin'].tolist()
print('Tahmini Üretim: ',np.round(tahmin))
print('Gerçek Üretim: ', np.array(data['kWh']).astype('int')[::200])
