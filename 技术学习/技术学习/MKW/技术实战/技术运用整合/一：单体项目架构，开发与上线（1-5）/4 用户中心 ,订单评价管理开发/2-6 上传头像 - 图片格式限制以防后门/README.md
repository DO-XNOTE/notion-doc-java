---
title: 2-6 上传头像 - 图片格式限制以防后门
---

# 2-6 上传头像 - 图片格式限制以防后门

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c9f51bec-67de-422f-b2b8-7961179f22b5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U364EOUM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDtM76SQMOH704gWtGe4AHlDVSaE2l3gtxz4Cc8BWuoQIgSjW2lFAYOSCziQ%2BCt7HmEzo00MbnVZG%2BNySDAN%2BWQS4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGqXtR8yGqPfNIgs8yrcA3F6GHYlzdbInnRVIn%2B%2FbZZMDFhOeZkGvIEDRZropMu8BbD4jij0KgzLwbQxe2DG3verp9zJT5PTF5xQyUsN%2F%2FsKnvohZNkzCqb%2BFP2ewL6ZMyxOQhFTEZB6tHeQ7kEFOqMWg%2FgV6KxD3%2FDTbMx1PX2Jclffxv8rJMQF8Q4I5l8Fth55PFPh0uk%2FnVek%2BEouD1OA8MBInt3EGiUujZW3IQxsEw9SsaKOcSQflZoT5KwJPBrFiwBvVmaEkrPmrpY8bmbrgIfpkOle3606IL2Jm2YviBlocSInvdIZFFDXCqT3B821vLaeR2Brghie9GqEN21rDquM53BaRnSmuJMq9K5NQjqgIekPTfAPSKsMaN4OgaxCNbObHmM7xxrEumZo1AILFgWsBgc8R1owXYL0%2FDnux1lJbc9nqZ3ux0%2B7Fq285h5B%2F6uYvrrVFxa%2BtEQVHJSTuy5jxtKHU%2BbbTplFNlrnklWodJVihcVXfMNu0MUtVHKVR5bIDuB2f5tnV%2BUz5e8u8r2hdhJ27eS%2BBKpUAG5SSY%2FJe3iVokvjOx3G%2Fu5SIuNKG0TfIdAiQTxzND9Zq7prZeKISef29Tg9atls8NT%2F9xYty9Z12fwlcK7Vyfqa3hc%2BiPA5huSlZtbeMJK4%2F9IGOqUB4qso3pUCIlZIMwMp1QGrErd%2FkzE8bUJGdd8qJ1bLb067wN8KLFKaFTlLeOqW2C9UufgDyA8WSnhJaxMJTI%2BR1eK0fcxNqcF1cDwhr%2FUWAQIE8K0czzXhaRyyKXdTqsCIubshbhxAPQhSh8wZweF%2BdgHNmoq%2FuoxIT1icUXwPxlAq4JDnuhlIlmsF%2BCHAq8UXxd%2BDz5Nk5XzWKB2BVw0cNG81uH59&X-Amz-Signature=61ceb12081af551a03f7b3a5f5bcad1ed782d024a660daa4a4d49539601432de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们的一个头像是可以正确的上传到咱们的服务器了，并且在网页端刷新以后也能够正常的展示。当然在数据库里面可以看到这一条，新的数据也能够更新到数据库里面都没有问题。但是在我们的代码里面其实有一个小的漏洞，或者是一个小的后门是值得我们去注意的。


我们在进行一个文件上传的时候，其实前端为我们进行了一个选择，它只限制了 JPG 和 PNG 的一个图片选择，选择了相应的图片，你才能够去进行上传。其实我们在这里也可以看得出来，我们点击头像，在这里面相应的 PNG 和 JPG 是可以去进行选择的，它都是一个量对的，但是像这是一个 gif 的格式，我们是选择不了，这个是由前端代码去控制的。但是如果你的一个接口被一些黑客去攻击，它是不会访问你的前端的，它会直接攻击你的接口。攻击 upload face。直接攻击它的时候，由于我们的后端 file 没有去校验它的一个文件的格式，所以对于黑客来讲，它就有可能会在你的服务器上去上传一些像点 sh、点  php 这样的一些文件。一旦文件成功的上传到你的服务器，对方就可以通过你的浏览器来访问到相应的一个文件了。这样子是非常非常危险的，是不可以去这样子做的。我们在很多年前就遇到过这种情况，有这样的一个漏洞，所以才导致我们的一个服务器被攻击的，这样子会非常的不好。所以你作为架构师，当你接到这样的需求，涉及到文件需求的时候，你就知道要存在这种情况。所以在让相关的开发人员去做的时候，你应该要告知他，你应该要去处理一下相应的。


一个后缀名的判断是一定要去判断的，哪怕对方没有错。在你进行代码 review 的时候，你也应该要关注一下的代码，他有没有去做一个判断。如果没有做判断，代码是不能够提交到服务器的，因为这就是一个服务器里面的后门，一定要去注意。所以在我们的地方，当我们拿到后缀名了以后，在这里我们一定要去把后缀名去做一个判断。OK，在这里我们来加一下。在这边加上一个相应的判断。要判断suffix，点 equals 忽略大小写。在这边我们限制一个是PNG，如果萨菲克斯是和偏激不同，再加一个，并且下一个是 JPG，都要去加一下。再加一个。总共是有三项，这一定要去注意的。写一下 jpg 和 jpeg 这样子三个判断。如果它都不满足，在这里我们就可以去远蹭。 return 一下 m Jason result 点 error message。


直接说图片格式不正确。OK，好，我们现在就可以来做一个测试。重启一下服务器在我们前端。在这里由于是我们设置的一个格式，所以在这边我们可以来开放一个 g i f，我们可以加一下，在后方，这里面我们也能够加一下，这样子我们就可以去进行一个选择了。好，我们到前端去刷新一下，在这里打开以后， g f 的文件就已经是亮了，选择点击上传，这个时候会提示图片格式不正确，我们的现在的校验就已经是成功了。这一点是一定要注意。在你做文件上传的时候是什么格式，一定要去做判断，哪怕在有些情况下是上传大量的不同格式的文件，你也应该要去做一个限定，只能够限制某些文件去做一个上传，这一点一定要去做的。

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

