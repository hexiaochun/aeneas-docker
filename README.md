


# aeneas-docker

[Aeneas](https://www.readbeyond.it/aeneas/) automatically generates a synchronization map between a list of text fragments and an audio file containing the narration of the text. In computer science this task is known as (automatically computing a) forced alignment.

## Running
First download docker and docker-compose.
Second download the code.
Then run the aeneas docker use the following.

```bash
sudo docker-compose up
```

## Usage

Run without arguments to get the usage message:

```bash
 sudo docker-compose run aeneas python3 -m aeneas.tools.execute_task
 sudo docker-compose run aeneas python3 -m aeneas.tools.execute_job

```
You can also get a list of live examples that you can immediately run on your machine thanks to the included files:

```bash
 sudo docker-compose run aeneas python3 -m aeneas.tools.execute_task \
   test.mp3 \
   test1.txt \
   "task_language=eng|os_task_file_format=json|is_text_type=plain" \
   map.json .

```



```bash
 sudo docker-compose run aeneas python3 -m aeneas.tools.execute_task test.mp3 test1.txt "task_language=eng|os_task_file_format=json|is_text_type=plain" map1.json .

```

```构建镜像
docker build -t zimu .

```启动接口
docker run -p 80:80 -d zimu

```测试接口
curl -X POST "http://localhost:80/generate_subtitles/" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "audio=@ceshi.mp3" -F "text=@ceshi.txt"


## License
[GNU AFFERO GENERAL PUBLIC LICENSE](https://github.com/oyekamal/aeneas-Docker/blob/main/LICENSE)
