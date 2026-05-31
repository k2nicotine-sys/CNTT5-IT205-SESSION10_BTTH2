playlist = []


def input_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
while True:

    choice = input_integer("""
========== PLAYLIST MANAGEMENT ==========
1. Thêm bài hát
2. Xem danh sách phát
3. Xóa bài hát
4. Sắp xếp và Trích xuất
5. Thoát

Mời bạn chọn chức năng:
""")

    match choice:
        case 1:
            sub_choice = input_integer("""
1. Thêm vào cuối danh sách
2. Chèn vào vị trí bất kỳ
Lựa chọn:
""")
            song_name = input("Nhập tên bài hát: ")
            match sub_choice:
                case 1:
                    playlist.append(song_name)

                    print("Thêm bài hát thành công!")
                    print(f"Số lượng bài hát hiện tại: {len(playlist)}")

                case 2:

                    index = input_integer("Nhập vị trí muốn chèn: ")
                    if index < 0 or index > len(playlist):
                        print("Vị trí không hợp lệ.")
                    else:
                        playlist.insert(index, song_name)
                        print("Thêm bài hát thành công!")
                        print(f"Số lượng bài hát hiện tại: {len(playlist)}")
                case _:
                    print("Lựa chọn không hợp lệ.")

        case 2:

            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
            print("==== DANH SÁCH PHÁT =====")
            for index, song in enumerate(playlist, start=1):
                print(f"{index}. {song}")
        case 3:
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
            sub_choice = input_integer("""
1. Xóa theo tên bài hát
2. Xóa theo số thứ tự

Lựa chọn:
""")
            match sub_choice:
                case 1:
                    song_name = input("Nhập tên bài hát cần xóa: ")
                    if song_name in playlist:
                        playlist.remove(song_name)
                        print(f"Đã xóa bài hát '{song_name}' khỏi danh sách.")
                    else:
                        print("Không tìm thấy bài hát trong danh sách phát.")

                case 2:
                    index = input_integer("Nhập số thứ tự cần xóa: ")
                    real_index = index - 1
                    if real_index < 0 or real_index >= len(playlist):
                        print("Vị trí không hợp lệ.")
                    else:
                        deleted_song = playlist.pop(real_index)
                        print(f"Đã xóa bài hát '{deleted_song}' khỏi danh sách.")
                case _:
                    print("Lựa chọn không hợp lệ.")
        case 4:

            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue

            sub_choice = input_integer("""
                    1. Sắp xếp A-Z
                    2. Trích xuất 3 bài hát đầu tiên
                    Lựa chọn:
                    """)
            match sub_choice:
                case 1:
                    playlist.sort()
                    print("\nDanh sách sau khi sắp xếp:")
                    for index, song in enumerate(playlist, start=1):
                        print(f"{index}. {song}")
                case 2:
                    first_three = playlist[:3]
                    print("\n3 bài hát đầu tiên:")
                    for index, song in enumerate(first_three, start=1):
                        print(f"{index}. {song}")
                case _:
                    print("Lựa chọn không hợp lệ.")
        case 5:
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
        case _:

            print("Lựa chọn không hợp lệ.")