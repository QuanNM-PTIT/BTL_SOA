# ĐỀ TÀI: HỆ THỐNG LÀM BÀI TRẮC NGHIỆM
## I. Giới thiệu thành viên:
- Nguyễn Mạnh Quân - B20DCCN550
- Nguyễn Sơn Hà - B20DCCN214
- Nguyễn Văn Mạnh - B20DCCN429
## II. Giới thiệu đề tài:
> Khi người dùng bắt đầu một bài thi, hệ thống sẽ truy xuất danh sách
> sinh viên để lấy thông tin sinh viên vào làm bài. Hệ thống truy xuất
> danh sách bài thi để xác minh thông tin bài thi và thông tin sinh viên.
> Khi các thông tin hợp lệ, hệ thống truy xuất danh sách câu hỏi tương
> ứng với bài thi và hiển thị ra màn hình.

 - Usecase: Tạo một bài thi khi nhận được yêu cầu.
## III. Công nghệ sử dụng:
- Back-end: FastAPI.
- Front-end: VueJs, Ant design.
- Database: MongoDB.
- Websockets.
- Deployment: Deta Space Cloud, Digital Ocean Cloud, Gitlab CI/CD.
## IV. Phân tích:
### 1. Quy trình làm bài thi trắc nghiệm gồm các hoạt động chi tiết sau:
	- Bước 1: Sinh viên bấm nút “Bắt đầu làm bài" .
	- Bước 2: Nhận thông tin chi tiết về sự kiện.
	- Bước 3: Hệ thống truy xuất dữ liệu thông tin của sinh viên và bài thi.
 	- Bước 4: 
  		+ Nếu thông tin hợp lệ chuyển sang bước 5.
		+ Nếu thông tin không hợp lệ quay lại bước 1.
  	- Bước 5: Hệ thống truy xuất dữ liệu thông tin các câu hỏi trong bài thi và hiển thị ra màn hình
### 2. Phân tích quy trình nghiệp vụ:
- Quy trình làm bài thi được chia thành các hành động sau:
	+ Sinh viên bấm nút bắt đầu làm bài.
    + Nhận thông tin chi tiết về sinh viên.
    + Nhận thông tin chi tiết về bài thi.
    + Xác minh chi tiết thông tin.
    + Nếu thông tin không hợp lệ (sinh viên không nằm trong danh sách hoặc bài thi chưa. bắt đầu) thì kết thúc quá trình.
    + Nếu thông tin hợp lệ thì lấy thông tin bài thi và hiển thị.
![SOA2](https://github.com/jnp2018/midproj-550214429/assets/84088181/268e4e2a-b4a3-4d3d-afbf-4eb3250cea19)


### 3. Lọc ra các hành động không phù hợp:
- Một số hoạt động không phù hợp tự động hóa hoặc đóng gói dịch vụ sẽ bị gạch bỏ:
   + Nhận thông tin chi tiết về sinh viên.
   + Nhận thông tin chi tiết về bài thi.
   + Xác minh chi tiết thông tin.
   + Nếu thông tin không hợp lệ (sinh viên không nằm trong danh sách hoặc bài thi chưa. bắt đầu) thì kết thúc quá trình.
   + Nếu thông tin hợp lệ thì lấy thông tin bài thi và hiển thị.
   + ~~Sinh viên chọn đáp án.~~
   + ~~Sinh viên nhấn nút nộp bài.~~
   + Thời gian làm bài kết thúc hệ thống tự động nộp bài.
   + Nhận thông tin chi tiết bài làm.
   + Nhận thông tin chi tiết sinh viên.
   + Xác minh thông tin chi tiết.
   + Đánh giá kết quả bài làm.
   + Đưa ra kết quả và lưu lại.
   + Gửi kết quả làm bài cho sinh viên.
   + ~~Sinh viên gửi thắc mắc về kết quả bài thi.~~
   + ~~Giải đáp thắc mắc cho sinh viên.~~
### 4. Xác định Entity service:
- Bằng cách phân tích các hành động còn lại từ B2, phân loại những hành động được coi là bất khả tri. Những hành động không theo bất khả tri được in đậm:
	+ **Sinh viên bấm nút bắt đầu làm bài.**
	+ Nhận thông tin chi tiết về sinh viên.
	+ Nhận thông tin chi tiết về bài thi.
	+ **Xác minh chi tiết thông tin.**
	+ **Nếu thông tin không hợp lệ (sinh viên không nằm trong danh sách hoặc bài thi chưa. bắt đầu) thì kết thúc quá trình.**
	+ **Nếu thông tin hợp lệ thì lấy thông tin bài thi và hiển thị.**
	+ **Thời gian làm bài kết thúc hệ thống tự động nộp bài.**
	+ Nhận thông tin chi tiết bài làm.
	+ Nhận thông tin chi tiết sinh viên.
	+ **Xác minh thông tin chi tiết.**
	+ Đánh giá kết quả bài làm.
	+ **Đưa ra kết quả và lưu lại.**
	+ **Gửi kết quả làm bài cho sinh viên.**

- Các hành động bất khả tri được phân loại Entity service sơ bộ và được nhóm lại thành Entity service sau:
	+ Student-Service: Là 1 service quan trọng của hệ thống. Service này cung cấp thông tin liên quan đến sinh viên. Get details cho phép truy xuất thông tin chi tiết của sinh viên.
![2](https://github.com/jnp2018/midproj-550214429/assets/84088181/9db0720a-8de6-4a07-a90f-59ede5aabc24)
	+ Test-Service: Là 1 service quan trọng của hệ thống. Service này cung cấp thông tin liên quan đến bài thi. Get details cho phép truy xuất thông tin chi tiết của bài thi.
![3](https://github.com/jnp2018/midproj-550214429/assets/84088181/81122673-d6d9-4037-a7f5-1b7004c67705)
	+ Question-Service: Là 1 service quan trọng của hệ thống. Service này cung cấp thông tin liên quan đến các câu hỏi trong bài thi. Get details cho phép truy xuất thông tin chi tiết của câu hỏi.
![4](https://github.com/jnp2018/midproj-550214429/assets/84088181/4a0fef46-4ebb-46c3-aa46-2ae880dc069c)
- Hành động còn lại được đặt sang 1 bên khi các Utility service được mô hình hóa ở phần sau:
	+ Gửi thông báo kết quả bài thi cho sinh viên.
### 5. Xác định logic cụ thể cho quy trình:
- Bước này được đề ra để xác định Task service. Các hành động không tuân theo bất khả tri vì chúng được quy định cụ thể cho quy tình làm bài thi:
	+ **Sinh viên bấm nút bắt đầu làm bài. (*)**
	+ **Xác minh chi tiết thông tin.**
	+ **Nếu thông tin không hợp lệ (sinh viên không nằm trong danh sách hoặc bài thi chưa. bắt đầu) thì kết thúc quá trình.**
	+ **Nếu thông tin hợp lệ thì lấy thông tin bài thi và hiển thị.**
	+ **Thời gian làm bài kết thúc hệ thống tự động nộp bài.**
	+ **Xác minh thông tin chi tiết.**
	+ **Gửi kết quả làm bài cho sinh viên.**
- Hành động đầu tiên trong danh (*) sách này tạo thành 1 cơ sở cho ứng viên năng lực dịch vụ, được viết ngắn gọn là TakeTheTest.
- Các hành động in đậm còn lại không tương ứng với các ứng viên năng lực dịch vụ. Thay vào đó chúng được xác định là logic xảy ra nội bộ trong TakeTheTest-Service.
![5](https://github.com/jnp2018/midproj-550214429/assets/84088181/c37e2180-fa79-42b3-86f4-529072045596)
### 6. Xác định các nguồn lực:
- Sau khi xem xét các yêu cầu xử lý của các ứng viên năng lực dịch vụ đã được định nghĩa cho đến nay, các tài nguyên tiềm năng sau đây đã được xác định:
	+ /Process/
	+ /Application/
	+ /Student/
	+ /Test/
	+ /Question/
	+ /Notification/
- Bởi vì quá trình mô hình hóa dịch vụ đã tạo ra 1 tập hợp các Entity Service, mỗi dịch vụ đại diện cho 1 thực thể, nên quyết định thiết lập 1 số ánh xạ sơ bộ giữa các tài nguyên đã xác định và các thực thể, như bảng dưới đây:

| Entity 	| Resource 	|
|:---:	|:---:	|
| Student 	| /Student/ 	|
| Test 	| /Test/ 	|
| Question 	| /Question/ 	|

### 7. Liên kết năng lực dịch vụ với tài nguyên phương thức:
- Mở rộng các Entity Service ban đầu bằng cách thêm phương thức phù hợp:
	+ TakeTheTest service (Task): Thông tin sinh viên làm bài thi là đầu vào chính để khởi động quy trình làm bài thi là ứng dụng do sinh viên yêu cầu. Start cần 1 phương thức POST để chuyển tiếp đầu vào đến 1 tài nguyên.
![6](https://github.com/jnp2018/midproj-550214429/assets/84088181/f42b3311-0d06-4ab2-a6cc-1b2f150ca31b)
	+ Student service(Entity): Ứng viên năng lực dịch vụ GetDetails được nối với phương thức GET cộng với tài nguyên /student/.
![7](https://github.com/jnp2018/midproj-550214429/assets/84088181/f200eaac-5469-4645-95a8-e37c62d654b4)
	+ Test service(Entity): Ứng viên năng lực dịch vụ GetDetails được nối với phương thức GET cộng với tài nguyên /test/.
![8](https://github.com/jnp2018/midproj-550214429/assets/84088181/0b6aedb7-a240-403d-9b79-21e35a793094)
	+ Question service(Entity): Ứng viên năng lực dịch vụ GetDetails được nối với phương thức GET cộng với tài nguyên /student/.
![9](https://github.com/jnp2018/midproj-550214429/assets/84088181/2aa583dc-b58a-465c-94e5-e60856196fe0)

### 8. Áp dụng hướng dịch vụ:

- Tài liệu quy trình kinh doanh sử dụng làm đầu vào cho quá trình mô hình hóa dịch vụ có thể cung cấp mức độ kiến thức về quá trình xử lý được yêu cầu bởi từng ứng viên năng lực dịch vụ REST đã được xác định.

- Hình thành thêm định nghĩa và phạm vi của khả năng dịch vụ, cũng như các ứng viên dịch vụ lớn, bằng cách xem xét tập hợp phù hợp của các nguyên tắc định hướng dịch vụ.

### 9. Xác định ứng viên thành phần dịch vụ:

- Trong mỗi trường hợp, TakeTheTest-Service gọi các Student-Service, Question-Service, Test-Service. Test-Service tiếp tục sinh ra 1 Notification Utility Service.

![10](https://github.com/jnp2018/midproj-550214429/assets/84088181/bfa92836-9a47-485d-a763-491b4a217cdc)

![image](https://github.com/jnp2018/midproj-550214429/assets/116872032/c157ba79-bb14-4207-852f-24f34bc2b409)




### 10. Phân tích các yêu cầu xử lý:

- Ngoài các hành động gửi thông báo đã được xác định trước đó, dường như không còn yêu cầu thêm các chức năng tập trung vào tiện ích.

- Tuy nhiên, khi không có yêu cầu xử lý mới nào tập trung vào tiện ích được xác định, một mối quan tâm đã được đưa ra cụ thể liên quan đến hành động xác minh dữ liệu đang được đóng gói như phần của dịch vụ TakeTheTest.

- Để hoàn thành hành động này, Rules Utility Service bên ngoài sẽ cần được soạn thảo và gọi để hoàn thành việc xác minh.

- Do đó, phân loại hành động xác minh dữ liệu có yêu cầu xử lý quan trọng và chuyên biệt mà không thể đáp ứng nếu nó vẫn là 1 phần của việc triển khai dịch vụ nhiệm vụ, logic này cần được chuyển đến 1 microservice chuyên dụng.

### 11. Xác định ứng viên dịch vụ tiện ích:

- Ứng viên dịch vụ Notification: Hành động Send là một ứng viên năng lực dịch vụ, như một phần của dịch vụ tiện ích có tên là Notification. Hành động Send sẽ chấp nhận phạm vi giá trị đầu vào, cho phép nó phát hành thông báo.
![12](https://github.com/jnp2018/midproj-550214429/assets/84088181/d5dd2bb9-6a30-4bd5-a5ae-76bbccd5ff28)

- Ứng viên dịch vụ Notification: Hành động send được mở rộng phương thức POST và tài nguyên /Notification/.
![13](https://github.com/jnp2018/midproj-550214429/assets/84088181/d5eb6791-60d3-4477-8390-889f192dcd4a)

### 11. Xác định ứng viên Microservice:

- Để xác định xem liệu bất kỳ đơn vị nào của logic này có thể đủ điều kiện để được đóng gói bởi một dịch vụ riêng biệt hay không đề xuất ứng viên dịch vụ Microservice tên là Verify Application, với một ứng viên năng lực dịch vụ Verify.

### 12. Sửa đổi thành phần ứng viên dịch vụ:

- Sự kết hợp giữa TakeTheTest Service mở rộng với sự xuất hiện của Utility Service Notification cùng với Microservice Verify Application.
![14](https://github.com/jnp2018/midproj-550214429/assets/84088181/83a05a0d-ec8d-4fab-8110-d61dedbd5cce)

## V. Thiết kế:
### 1. Đặc tả OpenAPI 3.0:

- API Get Student Infomation:

```yaml
openapi: 3.0.0
info:
  title: Get Student Information API
  version: 1.0.0
paths:
  /students/{student_id}:
    get:
      summary: Get student information by ID
      parameters:
        - name: student_id
          in: path
          required: true
          schema:
            type: string
            description: Student ID
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  student_id:
                    type: string
                    description: Student ID
                  name:
                    type: string
                    description: Student's name
                  email:
                    type: string
                    description: Student's email
                  dob:
                    type: string
                    format: date
                    description: Student's date of birth
                  address:
                    type: string
                    description: Student's address
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid request
        '404':
          description: Student not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Student not found
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Internal server error occurred
securitySchemes:
  bearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

- API Check Eligibility:

```yaml
openapi: 3.0.0
info:
  title: Check Eligibility API
  version: 1.0.0
paths:
  /test/check-eligibility:
    post:
      summary: Check student eligibility to take the test
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                student_id:
                  type: string
                  description: Student ID
                test_id:
                  type: string
                  description: Test ID
                current_time:
                  type: string
                  format: date-time
                  description: Current time
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  eligible:
                    type: boolean
                    description: Indicates whether the student is eligible to take the test or not
                  message:
                    type: string
                    example: Student is eligible to take the test
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid request
        '404':
          description: Student or test not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Student or test not found
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Internal server error occurred
securitySchemes:
  bearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

- API Take The Test:

```yaml
openapi: 3.0.0
info:
  title: Take the test API
  version: 1.0.0
paths:
  /task/{id}:
    get:
      summary: Get test
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  test_id:
                    type: string
                    description: ID bài test
                  num_of_questions:
                    type: integer
                    description: Số câu hỏi
                  duration:
                    type: integer
                    description: Thời gian tính bằng phút
                  time_start:
                    type: string
                    format: date-time
                    description: Thời gian bắt đầu
                  time_end:
                    type: string
                    format: date-time
                    description: Thời gian kết thúc
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Yêu cầu không hợp lệ
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Lỗi máy chủ nội bộ
securitySchemes:
  bearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

- API Get Questions:

```yaml
openapi: 3.0.0
info:
  title: Get Questions from Test API
  version: 1.0.0
paths:
  /questions/{test_id}:
    get:
      summary: Get list of questions by test ID
      parameters:
        - name: test_id
          in: query
          required: true
          schema:
            type: string
            description: Test ID
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Question'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid request
        '404':
          description: Test not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Test not found
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Internal server error occurred

components:
  schemas:
    Question:
      type: object
      properties:
        question_id:
          type: string
          description: Question ID
        question_text:
          type: string
          description: Question text
        options:
          type: array
          items:
            type: string
          description: List of options
        correct_answer:
          type: string
          description: Correct answer
```

- API Submit Exam:

```yaml
openapi: 3.0.0
info:
  title: Submit Exam API
  version: 1.0.0
paths:
  /test/submit:
    post:
      summary: Submit test
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                student_id:
                  type: string
                  description: Student ID
                exam_id:
                  type: string
                  description: Exam ID
                answers:
                  type: array
                  items:
                    type: object
                    properties:
                      question_id:
                        type: string
                        description: Question ID
                      selected_answer:
                        type: string
                        description: Selected answer
                submission_time:
                  type: string
                  format: date-time
                  description: Submission time
      responses:
        '200':
          description: Successful submission
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Test submitted successfully
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid request
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Internal server error occurred
securitySchemes:
  bearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

- API Get Test Result:

```yaml
openapi: 3.0.0
info:
  title: Get Test Result API
  version: 1.0.0
paths:
  /test/get-test-result:
    get:
      summary: Get test result for a student
      parameters:
        - name: student_id
          in: query
          required: true
          schema:
            type: string
            description: Student ID
        - name: test_id
          in: query
          required: true
          schema:
            type: string
            description: Test ID
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  student_id:
                    type: string
                    description: Student ID
                  test_id:
                    type: string
                    description: Test ID
                  score:
                    type: number
                    description: Test score
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid request
        '404':
          description: Student or exam not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Student or exam not found
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Internal server error occurred
securitySchemes:
  bearerAuth:
    type: http
    scheme: bearer
    bearerFormat: JWT
```

### 2. Sơ đồ tuần tự:

![image](https://github.com/jnp2018/midproj-550214429/assets/94891143/2aa72c82-711a-4fc3-aea4-aa52a287ea04)


### 3. Biểu đồ giao tiếp:
![image](https://github.com/jnp2018/midproj-550214429/assets/94891143/1a1ba211-8ca9-4929-bf7c-f716bf641212)






