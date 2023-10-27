# PDF批量转换工具

PDF批量转换工具是一款实用的Python GUI应用程序，旨在帮助用户轻松地将Word文档、图片批量转换为PDF格式。这款工具采用了简洁明了的用户界面设计，使得操作过程变得简单易懂。（PDF-Tool）

## 主要功能

- [X] Word转PDF：支持将Word文档批量转换为PDF格式。
- [X] 图片转PDF：支持将各种图片文件（如JPG、PNG）批量转换为PDF格式。
- [X] 批量转换：可以一次性选择多个文件，程序将进行批量转换，提高转换效率。
- [X] 自定义输出位置：可以选择输出PDF文件的保存位置，方便管理和查找转换后的文件。
- [X] 一键操作：程序的界面简洁明了，可以轻松地完成批量转换任务。

## 界面截图

<img src="https://raw.githubusercontent.com/wowqaqtat/PDF-Tool/main/docx/1.jpg" height="250px"> <img src="https://raw.githubusercontent.com/wowqaqtat/PDF-Tool/main/docx/2.jpg" height="250px">

<img src="https://raw.githubusercontent.com/wowqaqtat/PDF-Tool/main/docx/3.jpg" height="100px">

## 快速开始

1. 执行命令安装相关依赖库，如 `pip install tkinter`
2. 执行命令 `python main.py` 启动程序
3. 也可以执行 `pyinstaller -F -n PDF批量转换工具 main.py` 命令打包程序
4. 选择需要转换的文件，点击开始转换
   (注意：使用 `pyinstaller -F -w -n PDF批量转换工具 main.py` 命令，无法转换word文件(bug)，所以去掉 `-w` 参数)

**另外你也可以直接下载作者打包好的 `PDF批量转换工具.exe` 文件，`test文件夹` 中也提供了几个测试文件。**

## 测试流程

- [X] 正常选择一个或多个文件
- [X] 正常使用默认保存位置
- [X] 正常选择保存位置
- [X] 正常转换word为pdf
- [X] 正常转换png、jpg图片为pdf
- [X] 转换不支持的文件格式会提示错误
- [X] 未选择文件或未选择保存位置会提示错误

## 开发参考

开发者可以根据实际需要进行优化：

- [ ] 暂不支持包含批注的word文件，否则排版不美观
- [ ] 优化界面，使其更加美观
- [ ] 增加更多转换格式，如：BMP转PDF等
- [ ] 增加更多功能，如：PDF转word等

## 相关项目

- [图片加水印工具](https://github.com/wowqaqtat/Image-watermark-tool)：一款简单易用的图片加水印工具，可以帮助用户在图片上添加自定义的水印文字。（Image-watermark-tool）

## 联系我们

- 本程序基于 [MIT](https://opensource.org/licenses/MIT) 许可证开源。
- 本程序不定时更新，如果大家在使用的过程中，发现任何bug或有不错的想法，欢迎提出交流。
- 源代码：[https://github.com/wowqaqtat/PDF-Tool](https://github.com/wowqaqtat/PDF-Tool)
- 视频讲解：bilibili
- 邮箱：[help@haodukeji.cn](mailto:help@haodukeji.cn)
