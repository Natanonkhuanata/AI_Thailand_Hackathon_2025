
![enter image description here](https://upload.wikimedia.org/wikipedia/th/b/b5/CRMS6_logo.png)

##  AI  Thailand Hackathon 2025
ทีม ลูกพ่อขุนเม็งราย  รหัส  10022   

    ทีมของพวกเรามาจากโรงเรียนเทศบาล 6 นครเชียงราย

สมชิกทีม 
 - นายณฐนนท์  เขื่อนทา   ชั้นมัธยมศึกษาปีที่ 6     **(หัวหน้าทีม)**
 - นายภาคิน  วัฒนพีรพงศ์ ชั้นมัธยมศึกษาปีที่ 6  
 - นายกานต์กวี  อัศวโกวิทวงศ์  ชั้นมัธยมศึกษาปีที่ 6  
## นวัตกรรม

   **Classroom Safety** :  An AI-based system for detecting violence and identifying its location within the classroom (e.g., front or back). Enhances safety through real-time image detection and zone-based analysis.
   
 ระบบตรวจจับความปลอดภัยในห้องเรียน” เป็นนวัตกรรมที่ใช้เทคโนโลยีปัญญาประดิษฐ์ (AI) และการตรวจจับภาพ (Computer Vision) ในการเฝ้าระวังพฤติกรรมความรุนแรงหรือสิ่งผิดปกติที่เกิดขึ้นภายในห้องเรียน ระบบจะสามารถระบุพิกัดของเหตุการณ์ได้อย่างแม่นยำ เช่น เกิดขึ้นบริเวณหน้าห้อง กลางห้อง หรือหลังห้อง พร้อมวิเคราะห์ตำแหน่งเปรียบเทียบกับเงื่อนไขที่กำหนดไว้ล่วงหน้า เพื่อให้สามารถตอบสนองต่อเหตุการณ์ได้อย่างรวดเร็วและมีประสิทธิภาพ เพิ่มความปลอดภัยให้กับนักเรียนและครูผู้สอน

 - **Services of   AI  FOR  THAI**
	 - Person Detection   ระบบระบุตำแหน่งบุคคลในภาพ (Person Detection)
	 - Violence Classification  ระบบตรวจจับความรุนแรงจากภาพถ่าย (Violence Classification)

## Quiz

 - สร้าง API 2 ตัว:
   
   -   `API1`: รับ request จากผู้ใช้ แล้วเรียก `API2` ผ่าน HTTP
       
   -   `API2`: ตอบกลับข้อความเรียบง่าย
       
   -   ทั้งสองรันใน Docker และเชื่อมต่อกันด้วย `docker-compose`
   
   ## โครงสร้างโปรเจกต์ 	 	
   project-root/ 	
  ├── docker-compose.yml
  ├── api1/
  │   ├── Dockerfile
  │   └── app1.py
  └── api2/
      ├── Dockerfile
      └── app.py
     
   
   ## ภาษาในการพัฒนา
   
    -  Python 3
    -  Flask
   
   ## Docker  Desktop ใช้วิธีการสร้าง  Images เเละ  Container ด้วยวิธี ใช้ compose ที่จะสามารถติดตั้ง imageห เเละ containers หให้อัตโนมัติ 
   
       docker-compose up --build
       
   
   **Images ได้เเก่**
   
    -  ai_thailand_hackathon_2025-api1   port  8888:8888
       สำหรับ API1 จะต้องติดตั้งทั้ง Flask และ requests
   
       
     
    -  ai_thailand_hackathon_2025-api2   port  9999:9999
       สำหรับ API2 ติดตั้งเพียง Flask ก็เพียงพอ
   
   **Containers  ได้เเก่**
    - ai_thailand_hackathon_2025
   
   ## Docker-compose.yml
   
    - ไฟล์นี้ใช้กำหนด service ทั้งหมด 2 ตัว
    - ระบุว่า API1 ต้อง "รอ" ให้ API2 พร้อมก่อนจึงจะเริ่มทำงาน (`depends_on`)
    - Docker Compose จะสร้าง network ให้โดยอัตโนมัติ ทำให้แต่ละ container เรียกชื่อกันได้โดยใช้ชื่อ service คือ http://api2:9999/ 
   ในการใช้เรียก api2  
   
   ## ตรวจสอบการเชื่อมต่อเเละเเสดงผล
   
    - เมื่อ api1 เรียกใช้งาน api2 ได้สำเร็จ จะเเสดงที่ http://localhost:8888/ คือ
   
          {"Api1":"Hello this is API1","Api2_response":"Hello from API2 successfully  connected"}
   
    - api2 จะเเสดงที่  http://localhost:9999/  คือ
    
          "Hello from API2 successfully  connected"
