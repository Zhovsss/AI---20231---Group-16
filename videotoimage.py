import cv2
import os


def extract_frames(video_folder_path, output_folder):
    # Kiểm tra xem thư mục đầu ra có tồn tại chưa, nếu không thì tạo mới
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Số frame đã đọc
    frame_count = 0
    for video in os.listdir(video_folder_path):
        # Mở video để đọc
        cap = cv2.VideoCapture(video_folder_path+'/'+video)

        # Lấy tỷ lệ khung hình (FPS) của video
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            # Nếu không có thông tin FPS trong video, sử dụng một giá trị mặc định (ví dụ: 30 FPS)
            fps = 30

        while True:
            # Đọc từng frame
            ret, frame = cap.read()

            # Kiểm tra nếu hết video
            if not ret:
                break

            # Lưu frame vào thư mục đầu ra
            img_name = f"{output_folder}/frame_{frame_count:04d}.png"
            cv2.imwrite(img_name, frame)

            # Bỏ qua các frame để giữ mỗi giây 1 frame
            for _ in range(int(cap.get(cv2.CAP_PROP_FPS)) - 1):
                cap.read()

            frame_count += 1

        # Giải phóng tài nguyên
        cap.release()

    print(f"{frame_count} frames đã được tách và lưu trong thư mục {output_folder}.")


# Đường dẫn của video đầu vào
video_path = 'videos'

# Thư mục đầu ra cho các frame ảnh
output_folder = 'Image'

# Gọi hàm để tách video thành các frame
extract_frames(video_path, output_folder)

