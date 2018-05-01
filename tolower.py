import argparse
import io

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type=str, required=True)
    input_file = parser.parse_args().input_file

    with io.open(input_file,'r',encoding='utf8') as f:
        text = f.read()
        text = text.lower()

        output_file_name = "{}_lower.txt".format(input_file[:input_file.index('.')])
        output_file = open(output_file_name, 'w')
        output_file.write(text)
        output_file.close()


if __name__ == "__main__":
    main()