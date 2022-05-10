#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AuthException sẽ dừng bruteforcing (lỗi không mong muốn)
class AuthException(Exception):
    pass

# Một ngoại lệ RequestException có thể là do tắc nghẽn mạng và
# sẽ ngừng chạy bruteforcing chỉ sau một số trường hợp ngoại lệ tương tự liên tiếp
class RequestException(Exception):
    pass