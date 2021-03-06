/**************************************
*文件说明:httpd.h
*作者:高小调
*创建时间:2017年07月31日 星期一 19时16分18秒
*开发环境:Kali Linux/g++ v6.3.0
****************************************/
#include<wait.h>
#include<stdio.h>
#include<stdlib.h>
#include<sys/epoll.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<string.h>
#include<fcntl.h>
#include<sys/sendfile.h>
#include<pthread.h>
int get_listen_sock(int port);
void send_content_type(int sock,char *path);
int get_line(int sock,char *buff,int size);
void exec_cgi(int sock,char* method,char *path);
void send_error(int sock,int error_code);
void handle_http_request(int sock);
void handle_simple_get(int sock,char *path,int size);
int check_sock_connected(int sock);
void handler(int sig);

////////////多线程部分////////////
struct thread_arg{
	int epfd;
	int sock;
	struct epoll_event event;
};

void* thread_handle_http_request(void*);
