<h1>Gerçek Zamanlı Yüz Tanıma Sistemi, Proje Detayları:</h1>

![Deprem Verileri](https://raw.githubusercontent.com/kayaaicom/Yapay-Zeka-ile-Deprem-Tahmin-Ve-Analiz-Programi/main/mevcut-deprem-verileri.PNG)


Bu proje, gerçek zamanlı bir yüz tanıma sistemi oluşturmak için Python programlama dilini ve birkaç popüler kütüphaneyi kullanır. face_recognition, cv2 (OpenCV), PIL (Python Imaging Library), ve Tkinter kütüphanelerinin gücünden yararlanarak, kullanıcıların önceden tanımlanmış yüzleri bir video akışı içinde tanımasına ve bu yüzlerle ilişkilendirilmiş bilgileri grafiksel bir kullanıcı arayüzü (GUI) üzerinde görüntülemesine olanak tanır. Sistem, güvenlik, kişisel asistan uygulamaları, katılımcı takibi gibi çeşitli alanlarda uygulanabilir.

<p>Bu projenin savunma sanayi alanında en faydalı katkılarından biri, güvenlik ve izleme sistemlerinin geliştirilmesinde önemli bir rol oynamasıdır. Gerçek zamanlı yüz tanıma teknolojisi, aşağıdaki gibi çeşitli uygulamalarda kullanılarak savunma ve güvenlik alanındaki operasyonların etkinliğini artırabilir:</p>

<b>Erişim Kontrolü ve Kimlik Doğrulama:</b> Askeri tesisler gibi yüksek güvenlik gerektiren alanlarda, yetkisiz erişimin önlenmesi kritik öneme sahiptir. Yüz tanıma teknolojisi, belirli alanlara erişimi kontrol etmek ve sadece yetkilendirilmiş personelin giriş yapmasına izin vermek için kullanılabilir. Bu, geleneksel kimlik doğrulama yöntemlerine kıyasla daha güvenilir ve hızlı bir çözüm sağlar.

<b>Güvenlik Kameraları ve İzleme Sistemleri:</b> Yüz tanıma teknolojisi, güvenlik kameraları aracılığıyla sürekli izlenen alanlarda şüpheli veya aranan kişileri otomatik olarak tespit etmek için kullanılabilir. Bu, potansiyel tehditlerin erken uyarılarını sağlayarak proaktif güvenlik önlemlerinin alınmasına olanak tanır.

<b>Personel ve Ziyaretçi Yönetimi:</b> Askeri üslerde veya savunma sanayi tesislerinde personel ve ziyaretçilerin takibi için yüz tanıma sistemleri kullanılabilir. Bu, alandaki herkesin kimliğini ve konumunu gerçek zamanlı olarak izlemeye yardımcı olur, böylece olağanüstü durumlarda hızlı hareket edilebilir.

<b>Biyometrik Günlükler:</b> Yüz tanıma, personelin giriş-çıkış saatlerini kaydetmek ve bu bilgileri güvenlik veya çalışma saatlerinin denetimi için kullanmak üzere biyometrik günlükler oluşturmakta kullanılabilir. Bu, kart veya şifre tabanlı sistemlere kıyasla daha güvenli ve manipülasyona daha az açık bir yöntemdir.

<b>Entegre Savunma Sistemleri:</b> Yüz tanıma teknolojisi, daha geniş savunma ve güvenlik sistemlerine entegre edilebilir. Örneğin, dronlar ve diğer izleme araçları tarafından toplanan görüntüler, yüz tanıma algoritmaları kullanılarak analiz edilebilir, bu da geniş alanların etkin bir şekilde izlenmesini ve hızlı tepki verilmesini sağlar.

Yüz tanıma teknolojisinin bu ve benzeri uygulamaları, savunma sanayinde operasyonel güvenliği ve etkinliği artırma potansiyeline sahiptir. Ancak, bu teknolojinin kullanımı aynı zamanda mahremiyet ve etik konuları da beraberinde getirir, bu nedenle dikkatli bir şekilde yönetilmesi ve uygulanması gerekmektedir.

<h2>Gereksinimler</h2>
Bu projeyi çalıştırmadan önce, sisteminizde Python yüklü olmalıdır. Ayrıca, face_recognition, opencv-python (cv2 için), Pillow (PIL için) ve tkinter kütüphanelerinin de yüklü olması gerekmektedir. Bu kütüphaneleri aşağıdaki pip komutları ile yükleyebilirsiniz:


    pip install face_recognition opencv-python Pillow

<h2>Adım Adım Kılavuz</h2>
Gerekli Kütüphaneleri İçe Aktarma:
İlk olarak, yüz tanıma ve GUI işlemleri için gerekli olan kütüphaneleri içe aktarın.

<h2>Tanıdık Yüzlerin Veri Setini Oluşturma:</h2>
known_faces_filenames listesi içindeki dosya adlarından yola çıkarak tanıdık yüzlerin veri setini oluşturun. Her bir yüz resmi için yüz kodlamalarını (face_encodings) ve kişilerin isimlerini (known_face_metadata) içeren listeleri doldurun.

<h2>GUI Oluşturma:</h2>
Tkinter kullanarak, tanınan kişilerin bilgilerini gösterecek bir pencere oluşturun. Bu pencere, tanınan kişinin adını ve soyadını gösterecek bir etiket (label) ve kamera görüntüsünü gösterecek bir görüntü etiketi (image_label) içermelidir.

<h2>Kamera Görüntüsünü Güncelleme ve Yüz Tanıma:</h2>
update fonksiyonu içinde, kamera görüntüsünü okuyun, RGB formatına dönüştürün ve Tkinter ile uyumlu hale getirin. Ardından, face_recognition kütüphanesini kullanarak yüz tanıma işlemini gerçekleştirin. Tanınan her yüz için, tanıdık yüzlerin veri setiyle karşılaştırma yapın ve en iyi eşleşmeyi bulun. Tanınan kişinin adını ve soyadını GUI'de güncelleyin.

<h2>GUI Döngüsünü Başlatma:</h2>
root.mainloop() fonksiyonu ile GUI'nin olay döngüsünü başlatın. Bu sayede, program arayüzü etkileşimli hale gelir ve kullanıcı girdilerine yanıt verebilir.

Kaynakların Temizlenmesi:
Program kapatıldığında, video_capture.release() fonksiyonu ile kamera kaynağını serbest bırakın.

<b>Katkıda Bulunma</b><br>
Bu proje, açık kaynaklıdır ve katkılara açıktır. İyileştirmeler, hata düzeltmeleri veya yeni özellikler eklemek için pull request'ler gönderebilirsiniz.
