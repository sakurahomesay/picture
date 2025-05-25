import webview
import os

def main():
    # 设置窗口大小
    window_width = 500
    window_height = 650

    # 获取当前目录下的速写PC.html文件路径
    html_file_path = os.path.join(os.getcwd(), "速写PC.html")

    # 检查文件是否存在
    if not os.path.exists(html_file_path):
        print(f"文件未找到: {html_file_path}")
        return

    # 创建窗口并加载HTML文件
    webview.create_window(
        "速写",  # 修改窗口标题为“速写”
        url=f"file://{html_file_path}",
        width=window_width,
        height=window_height,
        resizable=True
    )

    # 运行应用
    webview.start()

if __name__ == "__main__":
    main()



