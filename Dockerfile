# 使用 Python 3.9.0 的官方镜像作为基础镜像
FROM python:3.9.0

# 设置工作目录
WORKDIR /app

# 只安装必要的依赖项
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 清理不必要的文件
RUN rm -rf tests

# 使用多阶段构建
FROM python:3.9.0
WORKDIR /app
COPY . /app

# 环境变量
ENV SerP=5001 \
    WsIP="0.0.0.0" \
    WsP=5002

# 运行应用程序
CMD ["python", "main.py"]
