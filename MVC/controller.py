import os

def process_fine_tuning(training_data_path, model_path, fine_tuning_method):
    # ตรวจสอบว่ามีไฟล์ที่ระบุอยู่หรือไม่
    if os.path.exists(training_data_path) and os.path.exists(model_path):
        # หาขนาดของไฟล์ training data และ model
        training_data_size = os.path.getsize(training_data_path)
        model_size = os.path.getsize(model_path)

        # ตรวจสอบว่าเป็นการ Fine-Tuning แบบใด
        if fine_tuning_method == 'fully_fine_tuning':
            # Fully Fine-Tuning
            # จำลองเวลาที่ใช้ในการสร้างโมเดล
            time_taken = training_data_size  # วินาที
            memory_used = model_size          # ไบต์

        elif fine_tuning_method == 'quantized_fine_tuning':
            # Quantized Fine-Tuning
            # จำลองเวลาที่ใช้ในการสร้างโมเดล
            time_taken = training_data_size * 2  # วินาที
            memory_used = model_size / 4         # ไบต์

        else:
            return "Error: Unknown fine-tuning method specified."  # ข้อผิดพลาดเมื่อระบุวิธีการ Fine-Tuning ไม่ถูกต้อง

        # ส่งค่าผลลัพธ์กลับ
        return f"Fine-Tuning Method: {fine_tuning_method}\nTime Taken: {time_taken} seconds\nMemory Used: {memory_used} bytes"
    else:
        return "Error: One or both of the specified paths do not exist."  # ข้อผิดพลาดเมื่อพาธที่ระบุไม่มีอยู่
