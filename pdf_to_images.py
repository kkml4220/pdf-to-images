import os
import sys

from pdf2image import convert_from_path


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_output_dir_path():
    """アウトプットディレクトリのパスを取得

    Returns (str): アウトプットディレクトリの絶対パス
    """
    OUTPUT_DIR = os.path.join(BASE_DIR, "pages")

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    return OUTPUT_DIR


def get_relative_path(path):
    """相対パスを取得

    Returns (str): スクリプトからの相対パスを取得
    """
    return os.path.relpath(path, BASE_DIR).replace("\\", "/")


def save_pdf_pages_as_png(pdf_path):
    """pdfをpng画像にして保存
    Args:
        pdf_path: pdfファイルのパス
    """
    images = convert_from_path(pdf_path)
    output_dir_path = get_output_dir_path()
    print("## Pages\n")
    for i, image in enumerate(images):
        output_file_path = os.path.join(output_dir_path, f"page{i+1}.png")
        image.save(output_file_path, "PNG")
        print(f"![page{i+1}]({get_relative_path(output_file_path)})")


def main():
    args = sys.argv
    if len(args) != 2:
        file_path = input("pdfファイルのパスを入力してください:")
    else:
        file_path = os.path.abspath(args[1])

    if not os.path.exists(file_path):
        print("ファイルが見つかりません")
    else:
        save_pdf_pages_as_png(file_path)


if __name__ == "__main__":
    main()
