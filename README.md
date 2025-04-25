# Online-ta'lim API

## Authentication (Autentifikatsiya)
POST /api/auth/register/ - Ro'yxatdan o'tish

POST /api/auth/login/ - Tizimga kirish

POST /api/auth/logout/ - Tizimdan chiqish

POST /api/auth/token/refresh/ - JWT tokenni yangilash

## Users (Foydalanuvchilar)

GET /api/users/ - Barcha foydalanuvchilar ro'yxati

GET /api/users/{id}/ - Aniq foydalanuvchi ma'lumotlari

PUT /api/users/{id}/ - Foydalanuvchi ma'lumotlarini yangilash

GET /api/users/me/ - Joriy foydalanuvchi ma'lumotlari

## Categories (Kategoriyalar)

GET /api/categories/ - Barcha kategoriyalar ro'yxati

POST /api/categories/ - Yangi kategoriya qo'shish

GET /api/categories/{id}/ - Aniq kategoriya ma'lumotlari

PUT /api/categories/{id}/ - Kategoriya ma'lumotlarini yangilash

DELETE /api/categories/{id}/ - Kategoriyani o'chirish

## Courses (Kurslar)

GET /api/courses/ - Barcha kurslar ro'yxati

POST /api/courses/ - Yangi kurs qo'shish

GET /api/courses/{id}/ - Aniq kurs ma'lumotlari

PUT /api/courses/{id}/ - Kurs ma'lumotlarini yangilash

DELETE /api/courses/{id}/ - Kursni o'chirish

GET /api/courses/category/{category_id}/ - Ma'lum kategoriya kurslari

## Modules (Modullar)

GET /api/modules/ - Barcha modullar ro'yxati

POST /api/modules/ - Yangi modul qo'shish

GET /api/modules/{id}/ - Aniq modul ma'lumotlari

PUT /api/modules/{id}/ - Modul ma'lumotlarini yangilash

DELETE /api/modules/{id}/ - Modulni o'chirish

GET /api/modules/course/{course_id}/ - Ma'lum kurs modullari

## Lessons (Darslar)

GET /api/lessons/ - Barcha darslar ro'yxati

POST /api/lessons/ - Yangi dars qo'shish

GET /api/lessons/{id}/ - Aniq dars ma'lumotlari

PUT /api/lessons/{id}/ - Dars ma'lumotlarini yangilash

DELETE /api/lessons/{id}/ - Darsni o'chirish

GET /api/lessons/module/{module_id}/ - Ma'lum modul darslari

## Enrollments (Ro'yxatga olishlar)

GET /api/enrollments/ - Barcha ro'yxatga olishlar

POST /api/enrollments/ - Yangi ro'yxatga olish qo'shish

GET /api/enrollments/{id}/ - Aniq ro'yxatga olish ma'lumotlari

PUT /api/enrollments/{id}/ - Ro'yxatga olish ma'lumotlarini yangilash

DELETE /api/enrollments/{id}/ - Ro'yxatga olishni o'chirish

GET /api/enrollments/user/{user_id}/ - Ma'lum foydalanuvchi ro'yxatga olishlari

GET /api/enrollments/course/{course_id}/ - Ma'lum kurs ro'yxatga olishlari

## Progress (Progress)

GET /api/progress/ - Barcha progresslar

POST /api/progress/ - Yangi progress qo'shish

GET /api/progress/{id}/ - Aniq progress ma'lumotlari

PUT /api/progress/{id}/ - Progress ma'lumotlarini yangilash

GET /api/progress/enrollment/{enrollment_id}/ - Ma'lum ro'yxatga olish progressi

## Reviews (Sharhlar)7 endpoints

GET /api/reviews/ - Barcha sharhlar

POST /api/reviews/ - Yangi sharh qo'shish

GET /api/reviews/{id}/ - Aniq sharh ma'lumotlari

PUT /api/reviews/{id}/ - Sharh ma'lumotlarini yangilash

DELETE /api/reviews/{id}/ - Sharhni o'chirish

GET /api/reviews/course/{course_id}/ - Ma'lum kurs sharhlari

GET /api/reviews/user/{user_id}/ - Ma'lum foydalanuvchi sharhlari