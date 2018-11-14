def tank_callback():
    row_num = 0
    col_num = 0
    for i in hero_info_list:
        if i.get('is_tank'):
            # 处理图片
            locals()['img' + str(i)] = Image.open(i.get('img_path'))
            locals()['img' + str(i)] = ImageTk.PhotoImage(locals()['img' + str(i)])
            # 动态生成不同变量名的Label标签
            label_img = Label(frame, width=95, height=95, image=locals()['img' + str(i)])
            label_name = Label(frame, text=i.get('name'))
            # 将生成的标签进行布局
            label_img.grid(row=2 * (row_num // 10), column=col_num)  # 0 2 4 6 8
            label_name.grid(row=2 * (row_num // 10) + 1, column=col_num)  # 1 3 5 6 7 9
            row_num += 1
            col_num += 1
            # 如果列号为10时，重新设为0
            if col_num == 10:
                col_num = 0
        # 重新进入事件循环
    root.mainloop()