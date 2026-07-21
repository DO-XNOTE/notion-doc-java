---
title: 2-2 上传头像 - 上传到指定目录
---

# 2-2 上传头像 - 上传到指定目录

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d735420e-ac14-4bcf-b4eb-372e07ac78d4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4WCY7OK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDD%2BjQMFVcjMJvoKVm8LOsziFhvM7FKdG6SL3furBLZTAIhAIAQkc9LJaasM1Bk8Is0QMIM58qkRo3ZT8sl6jii5znqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtWQ2MccpivuAJ484q3AMqIRU4B41gilDKJd6RkzQlhjgqnhD9Z1ufrA8OYdfM1w4X%2BfFfh5V%2FLR62hWwnwZa4oKAUw3MdZqIh%2F%2BprkErXCLQ2kbZReS%2FMoaYDaAvJZDNsy48r9oZGIjT6ja4kGtSD6boQaeDpi23HpB47NHada%2FLut%2BrVHODZIdzBh5ZNgP%2FXCDIV8qU0EkcXT2oU%2F%2FX25ZNtWINTPqxnJc4ObCGVJ0tC%2BJI1JMoozIGuZuUIrrRyh8MXPiVTsuvBHZNNy7Qx6BCKE%2FMlcj5f9xmX2mMWpCFiiyOXytg%2F1KR5pzsn56C4cmv4KHrJIp%2FWz%2BrQFNNwj6NYHB%2Brh0k5mnjUVvp2%2B5HTuQXKkC52xM2b%2B%2BSXNdo8tbd41fEYqq%2B2DVnzkXN6G2JOMUyEUsS9S3cUjYUnTCpLh5HjWZH4G4FzCeH5VMQP6crFzumBZrSuzbITMRyUStmXRj8MVrL21U1gOJjl3TTdSgtpOzVO8MPbfpkUB0GqKK5GTq4qV2gNVb4HOAS%2FQ8vbQMLLKEGBZsXn5BjjzP6cfJ4wPlaMzlST%2FW8D%2FpuE6zG%2FjhkWf9BxfNt8jNQ%2BOqG4OzK%2FJpWKXAVqkXKZzHr5jaSvVsZHBpfoXsHcqPx4%2BmMh%2BYuIq9zXmTCtuv%2FSBjqkAbIPa58D9UbGGYB1w1uluGa%2FbU%2BZKqkKCzhtwW35RZ4FF6ZfSmHdn%2Bv5NypRS8hdOKNguNi71lwwq5mcKcVwvP8SyvH5hWVRyTDsUL6cOfk6%2FrLdDoNAp5Ixx%2BfgyUSzcjRNCCd3vMXtL%2F%2F9il36RqEtlihhc5sBXsRgukk8e1lHcHRBtHyuKg%2FKJptTUenL%2FPnolapKnWhkiHUkQiQu9Dfj%2Fmsg&X-Amz-Signature=20a488d968a3edd5b7ad8ab2a2a8f5b01b7820ee44a26ada1759a422af5e5a84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接下来我们应该要完善一下代码，把文件进行一个上传。首先我们是需要去获得文件上传的文件名称，在这里先定一下 string file main，等于通过这个file，它有一个方法叫做get，有一个 original file name，这就是一个文件的原始的文件名，可以这样子去获取的。获取了以后，其实我们也应该要在这里去进行一个判断。虽然绝大多数情况下文静林是不可能会为空的，但是我们要去操作字符串的类型的一个内容，我们应该要去判断一下，只要是。


Deep you. Cheers. It's not. 不亮眼不为空的情况下，我们才能够对文件名去做相应的处理。首先文件上传的时候，每一个文件都会有文件名的，但是在保存的时候，我们要形成一定的规范。我们可以这样子去保存。比方我们可以一个叫做 face 杠，再加上一个用户的 user ID，再加上点它的一个后缀名，比方是PNG。以这样的一种形式去进行保存。所以在这里我们就需要针对 file name 去做一个分割了。点有一个 split 方法，这是一个分割，分割文件的后缀0，前方是一个点点，我们要加上一个两个反形量，这样子我们就可以把文件去分割成一个数组。定一下，这是一个 file name，很瑞，加以上一个注释。


文件重命名。比方我们有一个文件名叫做 m 杠face，点 p n g。这是它的文件上传我们所获得的原始文件名。我们要把它更改。在这里是进行分割，分割完之后，它会变成一个宿主。在输出里面其实就是这样子的。一个是 m face，另外一个就是 p n g。随后我们应该要获取一下PNG。获取文件的后缀名。在这里应该是获得。从这个数字里面去获得。数组里面去获得。应该是当前数组的长度减掉余位，因为它的下标是从 0 开始的。这样子我们就可以去获取了。


这是一个 suffix 文件后缀名。好，OK。这些有了之后，随后我们就可以进行一个重组了。文件名称重组定一下 string new file name，等于在这里 face 杠。这些其实大家可以去自定义，你可以叫做face，也可以叫做 file image，都没有问题。拼接上一个 user ID， user ID 是这样子，直接拼接，再加上一个点后缀名，后缀名直接把 suffix 加过来。这样子我们的一个新的文件名就已经是重组成功了。但是在这种方式的使用之下，我们要注意，这种方式其实是属于一种覆盖式的。覆盖式上传，因为我们每次上传的某一个用户，他的头像，他的名称都是一模一样的，都是这样子的。如果你要使用增量式的，你要使用增量式，你需要在后面，你可以去把当前的一个年月日时分秒可以去加一下，这样子每次用户上传的一个头像，它的一个图片都会保存到咱们的服务器里面了，可以写一下。如果要增量式是需要额外拼接当前时间，这样子就 OK 了。


好。随后其实这些这一块内容是属于是我们的一个文件名的设置。接下来我们就要去设置一下我们的文件最终上传所保存的一个地址，这其实也是一个拼接上传的头像最终保存的位置。这个位置现在其实我们就应该要去做一个构建了，我们要使用 Fi file space 去加上这个文件，就是用户的 ID 前缀，再加上最终所重新定义的一个文件名，这样子就已经是编辑好了。但是在一定要注意文件名，在这里我们是没有加上一个斜杠，也就是分割符，在这里是务必要去加上一下的。好在我们来定义一下string，这是一个 final face pass，定这个名字。好。定义好了以后，在我们是需要去构建一个文件对象，我们构建一个file，取一个名字叫做 out file，等于在这里我们是直接可以把给用出来。在这里面会传入一个 u r i，它的一个地址，地址其实就是 final face pass，就是一个文件所要去保存的一个具体的路径，你是需要去设置进去的。


随后我们要去创建一下它的一个路径，因为我们在现在的一个文件夹里面，其实我们已经是创建到了 CSS 对吧，如果路径没有，我们应该要去把它的 parent 复制的，所有路径都要去生成一下。所以在这个地方我们应该要去做一个判断，它的 gets parents 有一个 parents file，判断一下要不为空。如果不为空的情况下，在这边我们就可以去做一个创建了，创建文件夹。


Hot fire gets parents. Fire! m k g i r s 这是一个。如果加上一个 s 就代表它是一种它的负极。目录都会去递归的生成的。它是可以生成多级的。好，这是一个生成。随后下一个。在这里我们就要来进行一个文件的输出，文件输出保存到目录。由于我们已经是构建了一个 out file，所以我们在这边要使用到一个 file output stream。我们要把它给 mule 出来。在这里把它的一个目标位置先写好。这是一个 out file。在这里会有一个 l 流的异常 file not found。这个我们先不管，我们还要再写一个 input stream。写完之后我们再把这两个异常统一的 try catch 一下。在这里我们再来构造一个 input string，这个主要是用于去获取它的文件输入流的。输入流其实就是在这里文件上传的时候，我们所获得的一个 multi pass file。从这个 file 里面我们就可以去获得了点 get input stream。拿到了以后，在它的下方我们就可以去做一个文件的保存。文件保存我们会有一个底窍，叫做 i o 有TOS。这个是在阿帕奇里面 comments 的一个包，在 l 留下的一个包。在这里使用它有一个方法叫做点copy，在这里面可以看到它。其实在这里面会有很多的一些方法，所以我们使用这个就可以了。它是一个 input stream，和一个 output stream。 input 相应，我们把 input stream 截过来output，把 file output stream 写过来，这样子它就可以去把一个文件做一个相应的上传了。在这里我们把整个方法进行一个 try catch，这样子刚刚的一个红色波浪线相应的异常就会被他所 catch 到。好。OK。但是我们还有一点是需要去注意的，因为我们在这里使用一个 file output stream 流，一旦使用完毕，你是需要去进行关闭的。所以我们在这个下方要去定义一个finally，我们要把提到上方，提到它的位置，咱有一个null，把这个给删掉。在这个下方我们就可以去做一个判断了。要判断一下，首先判断它不为空，如果不为空，我们就可以去进行一个关闭。我们先要 flash 一下，再来一个close，但是在这里它也会有相应的异常。所以在这个位置你也要去进行一个track，去把它给包一下 track 去，这样子其实我们就 OK 了，它就可以完成一个文件的上传了。好，接下来我们可以来做一个测试。我们来测试一下。在这里我们去重启一下服务器，我们的一个文件文件现在其实只到 faces 下方，只到faces，如果要去创建它赋值目录，其中就会包含一个当前文件所上传的一个用户，他的用户 ID 他也会去创建的。创建完毕目录了以后，他才可以去做一个运行的。在我们的控制台报了一个错，在这里看到有一个 center user Ctrl method，有一个我们的定义映射是出了问题，来看一下。有一个 update 已经是被创计了已经。现有的一个方法是在 user control 里面已经是包含了。所以我们在这里很明显是发生了一个问题，在这个位置写错了对吧？我们没有去更改。所以在我们要参考咱们的前端。前端的定义是一个 upload face，所以把拷贝贴到位置去覆盖一下就 OK 了。好，所以我们在遇到一些问题的时候不要怕，其实控制台上会把你的一些错误制描述的比较清晰，其实也是非常清楚的。根据他的错误日志去排除错误，这是一个非常好的方式。现在我们就启动 OK 了，清空一下控制台，我们到前端刷新一下。前端刷新以后，在这里我们来选择某一张图片，在这里我们来选择一个 face 1，选择之后，然后点击上传，在这里提示上传成功。上传成功以后，当前页面进行了一个刷新，但是图片还没有发生更改，但是没有关系，因为我们在代码里面还没有去把路径给返回出来。我们现在就可以去我们的当前的一个文件系统来看一下。在这里可以看到这是当前用户的一个 user ID，已经是创建好了。随后我们往下面看，这个时候你会发现有一张图片，这张图片就是我们刚刚所上传的。双击一下这一张图片，在这个图片里面，这个是我们对它进行的一个文件的重命名，其实是三个部分，一个是face，一个是用户ID，一个是后缀名PNG。这样子我们就已经是实现了文件的上传了。

```java
/**
 * <h1></h1>
 */
@SuppressWarnings("all")
@Api(value = "用户信息api接口", tags = "用户信息api接口")
@RestController
@RequestMapping("userInfo")
public class CenterUserController extends BaseController {

    @Autowired
    private CenterUserService centerUserService;

    @Autowired
    private FileUpload fileUpload;

    @ApiOperation(value = "用户头像修改", notes = "用户头像修改", httpMethod = "POST")
    @PostMapping("/uploadFace")
    public IMOOCJSONResult uploadFace(@ApiParam(name = "用户id", value = "userId", required = true) @RequestParam String userId,
                                               @ApiParam(name = "file", value = "用户头像", required = true)
                                                MultipartFile file,
                                                HttpServletRequest request, HttpServletResponse response) {
        // 定义头像保存的地址
//        String fileSpace = IMAGE_USER_FACE_LOCATION;
        String fileSpace = fileUpload.getImageUserFaceLocation();

        // 在路径上每一个用户增加一个userId，用于区分不同用户上传
        String uploadPathPrefix = File.separator + userId;
        // 开始文件上传
        if (file != null) {
            FileOutputStream fileOutputStream = null;
            InputStream inputStream = null;
            // 获取文件的上传的原始名称
            String fileName = file.getOriginalFilename();
            try {
                if (StringUtils.isNotBlank(fileName)) {

                    // 文件重命名 imooc-face.png -> ["imooc-face", "png"] 数组
                    /** String[] split = fileName.split("\\."); */
                    String fileNameArr[] = fileName.split("\\.");

                    // 获取文件的后缀名
                    /**int i = suffix.length - 1;*/
                    String suffix = fileNameArr[fileNameArr.length - 1];

                    /**
                     * 对上传文件的格式一定要进行限制，如果恶意的上传文件.php等上传的格式的程序，服务可能会受到网络攻击等危险
                     */
                    if (!suffix.equalsIgnoreCase("png") && !suffix.equalsIgnoreCase("jpg") && !suffix.equalsIgnoreCase("jpeg")) {
                        return IMOOCJSONResult.errorMsg("图片格式不正确");
                    }

                    // face-{userId}.png
                    // 文件名重组，覆盖式上传， 增量式:需要额外拼接当前时间
                    String newFileName = "face-" + userId + "." + suffix;

                    // 上传文件最终保存的位置
                    String finalFacePath = fileSpace + uploadPathPrefix + File.separator + newFileName;

                    // 用于提供给web服务访问的地址
                    uploadPathPrefix += ("/" + newFileName);

                    File outFile = new File(finalFacePath);

                    if (outFile.getParentFile() != null) {
                        // 创建文件夹
                        outFile.getParentFile().mkdirs();
                    }

                    // 文件输出保存的目录
                    fileOutputStream = new FileOutputStream(outFile);
                    inputStream = file.getInputStream();
                    /**
                     * Apache的IO流操作的的工具泪，可以直接使用
                     */
                    IOUtils.copy(inputStream, fileOutputStream);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (fileOutputStream !=null) {
                    try {
                        fileOutputStream.flush();
                        fileOutputStream.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        } else {
            return IMOOCJSONResult.errorMsg("上传文件不能为空！");
        }

        // 获得图片服务地址
        String imageServerUrl = fileUpload.getImageServerUrl();

        // 由于浏览器可能存在缓存的情况，所以在这里我们需要加上时间戳来保证更新后的图片可以及时的刷新
        String finalUserFaceUrl = imageServerUrl + uploadPathPrefix + "?t=" + DateUtil.getCurrentDateString(DateUtil.DATE_PATTERN);

        // 更新用户头像到数据库
        Users userResult = centerUserService.updateUserFace(userId, finalUserFaceUrl);

        userResult = setNullProperties(userResult);
        CookieUtils.setCookie(request, response, "user", JsonUtils.objectToJson(userResult), true);
        // TODO  后续要改， 增加令牌TOKEN，会整合进redis， 分布式会话

        return IMOOCJSONResult.ok();
    }
```

