# Changelog

## [0.3.27](https://github.com/PJendritza/mxbiflow/compare/v0.3.26...v0.3.27) (2026-11-02)


### Features

* :arrow_up: update dependencies and lockfile ([80ac4e9](https://github.com/PJendritza/mxbiflow/commit/80ac4e9e13a1f85859f9d57280858c89896bb7a8))
* :arrow_up: update pymxbi to 0.1.1 ([d265b06](https://github.com/PJendritza/mxbiflow/commit/d265b06f4204e0d2726e079f77237730bb3da34b))
* :arrow_up: update python t0 3.14 ([46d3b4b](https://github.com/PJendritza/mxbiflow/commit/46d3b4b7d19a2700a2e7029fe01a598150055bdd))
* :bento: add aplayer update and quit handling ([82998e2](https://github.com/PJendritza/mxbiflow/commit/82998e2be00c2a3ad300418d96dc5877b787305b))
* :bento: add assets directory and clicker sound path ([8f55742](https://github.com/PJendritza/mxbiflow/commit/8f55742e0c230d945851a21bcdcc7f6014bcdf8b))
* :bento: add assets module and clicker sound ([42176fc](https://github.com/PJendritza/mxbiflow/commit/42176fc9b631d2e379640d6376ef2fcec2e4c126))
* :bento: add level option 1 to animal card ([1c39d5e](https://github.com/PJendritza/mxbiflow/commit/1c39d5eee35d9ee1b226a07e0a69fce47bd0e16d))
* :bento: add SizeReduction scene and use ConfigStore ([4afb591](https://github.com/PJendritza/mxbiflow/commit/4afb591f99045fdd95ead9610b5b57c91e13e65b))
* :bento: add trial increment and reset methods ([337c484](https://github.com/PJendritza/mxbiflow/commit/337c4846140ac4c517a1c6b919c2040ac5cca9bf))
* :bento: add update method to MXBIFlow ([205290b](https://github.com/PJendritza/mxbiflow/commit/205290bc600918213feeff4b1a885b6ef39bc1ef))
* :fire: remove decide method from SceneProtocol ([13beb29](https://github.com/PJendritza/mxbiflow/commit/13beb292df364748a596a239fc7d0cf0094de55b))
* :fire: remove tkinter version config ([1df8df9](https://github.com/PJendritza/mxbiflow/commit/1df8df968b52ba9d450db0198e43c8e9169548df))
* :fire: remove tkinter version config panle ([6dc4074](https://github.com/PJendritza/mxbiflow/commit/6dc4074309543cdff56a8d7af77efebb6ab4103f))
* :fire: remove unused models and config files ([0ff227d](https://github.com/PJendritza/mxbiflow/commit/0ff227df4f1f754f2a06a6839cb1a106b2325c85))
* :heavy_plus_sign: add inflection dependency ([d03e71a](https://github.com/PJendritza/mxbiflow/commit/d03e71ab00edd7047e87df5adfc2fffbfd5fe4e9))
* :heavy_plus_sign: add loguru logging dependency ([456654e](https://github.com/PJendritza/mxbiflow/commit/456654eca1bb5bdb53323cfd99941a3742946d15))
* :heavy_plus_sign: add pygame-ce, pyside6, qtawesome dependencies and new entry point ([cabd684](https://github.com/PJendritza/mxbiflow/commit/cabd684eb157d53beef1ff42f3582963e7d8d6ea))
* :heavy_plus_sign: add pymotego dependency ([fabdb09](https://github.com/PJendritza/mxbiflow/commit/fabdb09cda94cd86f26e88c15df7d692212088ab))
* :heavy_plus_sign: add pymxbi ([b69aa39](https://github.com/PJendritza/mxbiflow/commit/b69aa39cb783bb469469825c82355b4339e4490d))
* :sparkles: add audio player integration ([c71c41c](https://github.com/PJendritza/mxbiflow/commit/c71c41c19526f03d84edaa24ca91cc5f6f66d981))
* :sparkles: add audio player module with pure tone generator ([c450792](https://github.com/PJendritza/mxbiflow/commit/c4507929afdf982cd7a702aec3c565a75781700e))
* :sparkles: add beam-break + RFID detector implementation ([c943a8b](https://github.com/PJendritza/mxbiflow/commit/c943a8bc117367e4ea085dec236e714fff061a8f))
* :sparkles: add CLI interface and MXBI core implementation ([e48d79e](https://github.com/PJendritza/mxbiflow/commit/e48d79e0979d4117be3b6188508bc9be7c4116bf))
* :sparkles: add data_dir property to MXBIFlow ([eab01d1](https://github.com/PJendritza/mxbiflow/commit/eab01d15a8bd211dae0adaf021a36ed6c8c884bc))
* :sparkles: add detector state machine implementation ([f2f6ddc](https://github.com/PJendritza/mxbiflow/commit/f2f6ddc25f3c324fc1566a51d0c03a7e7183e15a))
* :sparkles: add Dorset LID665v42 RFID reader driver ([c19f2db](https://github.com/PJendritza/mxbiflow/commit/c19f2db3c2a0c5f07ebc22c8fa6ae6e7a15aacc3))
* :sparkles: add dynamic level table support for stages ([d9f820b](https://github.com/PJendritza/mxbiflow/commit/d9f820b2241e0d758edf85f8a04a7eecdf2c86cc))
* :sparkles: add event bus implementation ([d145fcd](https://github.com/PJendritza/mxbiflow/commit/d145fcd42aaa708e55f4aef1e69bce429aeaceac))
* :sparkles: Add frequency response table support to audio player ([#16](https://github.com/PJendritza/mxbiflow/issues/16)) ([1c68750](https://github.com/PJendritza/mxbiflow/commit/1c687502979df723f0650b50a56c106fc9323a93))
* :sparkles: add initial habituation training task implementation ([b8a037f](https://github.com/PJendritza/mxbiflow/commit/b8a037fde8c99dfffae5fa4d8f55d9c8d60cae05))
* :sparkles: add initial habituation training task implementation ([1ce478d](https://github.com/PJendritza/mxbiflow/commit/1ce478d4b7e17e80c863e1bea7b1e85ab3401e49))
* :sparkles: add intensity control and upgrade to int32 audio ([e4ded6b](https://github.com/PJendritza/mxbiflow/commit/e4ded6b04786e0e258a50ccf52038a0c9c55a208))
* :sparkles: add mock detector implementation ([ae7a9b2](https://github.com/PJendritza/mxbiflow/commit/ae7a9b259e2acb4505d6e6d1a2095a73ce11c394))
* :sparkles: add mock rewarder and reward specifications ([046fd25](https://github.com/PJendritza/mxbiflow/commit/046fd252266c49ee249e8ec700c7c3300d2c786a))
* :sparkles: add persistent data tracking and display widget ([3e75fd9](https://github.com/PJendritza/mxbiflow/commit/3e75fd915e6a9d4e32ab1b116b187dbae92a60cc))
* :sparkles: add persistent data tracking and display widget ([279c21d](https://github.com/PJendritza/mxbiflow/commit/279c21da6a1b45cf9c86fe86564e664cbb0d186b))
* :sparkles: add platform module with PlatformEnum ([9a05432](https://github.com/PJendritza/mxbiflow/commit/9a0543284b8a60ca33945985c6554d81d4e0c32d))
* :sparkles: add poll interval and other fields to detector cards ([af92d4b](https://github.com/PJendritza/mxbiflow/commit/af92d4b89751bcaa26ba2e66bc6c028453a18510))
* :sparkles: add pump rewarder and update reward interface ([dae02cf](https://github.com/PJendritza/mxbiflow/commit/dae02cf7fcdc35a87da917754ca46e606087714d))
* :sparkles: add pydantic models and configuration builder ([63307ad](https://github.com/PJendritza/mxbiflow/commit/63307adc32c583ab2189c859268a3f34025854a1))
* :sparkles: add pydantic models for detector and rewarder configuration ([e245e17](https://github.com/PJendritza/mxbiflow/commit/e245e175c20d90a93d29d3eff6d289a7c78d389a))
* :sparkles: add rewarder duck type ([eaca244](https://github.com/PJendritza/mxbiflow/commit/eaca244c1364661eb5c179b47a4244d2191ca6b5))
* :sparkles: add RPI GPIO pump driver ([b85ad22](https://github.com/PJendritza/mxbiflow/commit/b85ad226fb338ff06191d2409e230776c5796275))
* :sparkles: add RPI IR break beam sensor driver ([280ed1b](https://github.com/PJendritza/mxbiflow/commit/280ed1b1875eb4c271a370c2abac523d633a7d0f))
* :sparkles: add rsync file sync helper ([5556951](https://github.com/PJendritza/mxbiflow/commit/55569519b46dcb05a6f305e3f3dc0f6b898dae68))
* :sparkles: add Samba mount systemd unit generator ([eb4e518](https://github.com/PJendritza/mxbiflow/commit/eb4e518030f9bd4a1c791dcafe4434df3eb98bcb))
* :sparkles: add screen module with Screen dataclass ([e263eca](https://github.com/PJendritza/mxbiflow/commit/e263eca0ef03affea813d925c7c9e494eaafae22))
* :sparkles: add screen size detection with pyglet ([c299fc8](https://github.com/PJendritza/mxbiflow/commit/c299fc89160c94dae4123181abd4be9a36c8a895))
* :sparkles: add screen size support to MXBI class ([87c1d04](https://github.com/PJendritza/mxbiflow/commit/87c1d04728c0afa32b1f07937d4bbcfce892f2cf))
* :sparkles: add serial utility functions for baudrates and ports ([23c91ea](https://github.com/PJendritza/mxbiflow/commit/23c91ea9c15fabfab9723e52ce5c3b9bf6e42767))
* :sparkles: add session counter path constant ([bf4c7c5](https://github.com/PJendritza/mxbiflow/commit/bf4c7c5aece1f868877ec13fb137faa5165a1c5d))
* :sparkles: add stages field to Options model ([13fc1bc](https://github.com/PJendritza/mxbiflow/commit/13fc1bc11e0850ef56cd4ea58c441ac5e73ab46f))
* :sparkles: add standard gate detector with state machine ([3fbdc69](https://github.com/PJendritza/mxbiflow/commit/3fbdc696a54a2a8f2decd494523ef12d7259854e))
* :sparkles: add support for standalone rfid detector ([#2](https://github.com/PJendritza/mxbiflow/issues/2)) ([1401b29](https://github.com/PJendritza/mxbiflow/commit/1401b29cec94a0e0be890d7fbda7a91a5dae4fd5))
* :sparkles: add task and level change logging to scheduler ([0bee0c0](https://github.com/PJendritza/mxbiflow/commit/0bee0c0f450c93f03dcdb7cefb77071977ec2a05))
* :sparkles: add through beam sensor duck type ([69c173c](https://github.com/PJendritza/mxbiflow/commit/69c173c253a3e979d68d0be5b675dcb9b006f4a4))
* :sparkles: add typer CLI dependency and entry point ([6c099c3](https://github.com/PJendritza/mxbiflow/commit/6c099c3eece3ffd375a1fced081d636b19a4a841))
* :sparkles: add vision detector base class ([a860437](https://github.com/PJendritza/mxbiflow/commit/a8604374ea1a743e7110754a277cf9d02732f088))
* :sparkles: add WAV caching and task cancellation to audio player ([fea4fd5](https://github.com/PJendritza/mxbiflow/commit/fea4fd53a80fe1bb2f9ed2caeb7e8a615c710591))
* :sparkles: amixer interface for linux ([acee101](https://github.com/PJendritza/mxbiflow/commit/acee1017db3d912978341f4925b629ddda56f860))
* :sparkles: enhance detection result with timestamp and animal_id ([07150bf](https://github.com/PJendritza/mxbiflow/commit/07150bfa86f078c9c3080072ecce579a2b59a2ac))
* :sparkles: enhance MockDetector with thread-safe detection simulation ([660a9be](https://github.com/PJendritza/mxbiflow/commit/660a9bee333d9126bc497d235fed9968fbe80037))
* :sparkles: enhance RPI GPIO pump with direction control stubs ([96f5703](https://github.com/PJendritza/mxbiflow/commit/96f5703673da3d3b8ad5c3daddcc3c0376669a3e))
* :sparkles: enhance state machine with animal detection handling ([683c1fa](https://github.com/PJendritza/mxbiflow/commit/683c1fa8925fe44de8b168ff233fc9e99405637b))
* :sparkles: Fully automatic habituation training ([79cae2d](https://github.com/PJendritza/mxbiflow/commit/79cae2d710a40e165dbb1097ee1d55953b090c42))
* :sparkles: introduce gpiozero && move rewarders to peripheral ([16ee623](https://github.com/PJendritza/mxbiflow/commit/16ee6232df76074d91de798d39ea64e12e56abd7))
* :sparkles: new logic habituation training: cumulative stay time ([3f1b756](https://github.com/PJendritza/mxbiflow/commit/3f1b756d9b0d2b4c86865f911b484503c5d66b5b))
* :sparkles: new logic habituation training: cumulative stay time ([45f7e94](https://github.com/PJendritza/mxbiflow/commit/45f7e9481f7ea07e53be49da9641892a56d12d3c))
* :sparkles: Optional persistence of level_trial_id ([d3da630](https://github.com/PJendritza/mxbiflow/commit/d3da63034ad96c1b2f210289cf01b12c833c1491))
* :sparkles: Optional persistence of level_trial_id ([fcfd483](https://github.com/PJendritza/mxbiflow/commit/fcfd483f5131008ad174653f6546437d5c11faa3))
* :sparkles: Provide temporary email and post-processing solutions ([4d03196](https://github.com/PJendritza/mxbiflow/commit/4d031960a5eb6151bb4d3229710042ff7c38ee75))
* :sparkles: Provide temporary email and post-processing solutions ([aa39ac1](https://github.com/PJendritza/mxbiflow/commit/aa39ac19056cb31a31af74e5cd50ae0c30e533b2))
* :tada: init pymxbi project ([83f42e1](https://github.com/PJendritza/mxbiflow/commit/83f42e1ba3ae3022c00eba672e93422ad94aebb4))
* ✨ A sound data synchronization mechanism ([a88fc89](https://github.com/PJendritza/mxbiflow/commit/a88fc89016cca84211ab069e3867e0dfad51b3dc))
* ✨ Adapt configuration interface to new bundle model for cross-modal task ([d5274d0](https://github.com/PJendritza/mxbiflow/commit/d5274d043ce59f5c0a1e290502c53043f36a039b))
* ✨ add auto start functionality and refactor save method ([19b3a3f](https://github.com/PJendritza/mxbiflow/commit/19b3a3f7e72b11e096f687b1d216bf78ca3e629a))
* ✨ add auto start functionality and refactor save method ([d3f1194](https://github.com/PJendritza/mxbiflow/commit/d3f1194caa40b54aa87f521153f5a10322383489))
* ✨ add bordered canvas component for visual scenes ([b51e575](https://github.com/PJendritza/mxbiflow/commit/b51e575575eb4a4f727c505540f77eda11501581))
* ✨ add bordered canvas component for visual scenes ([d49c8a9](https://github.com/PJendritza/mxbiflow/commit/d49c8a9e29f3c17be0b928070e3822a9211540d2))
* ✨ add center property to screen class ([8f6ea51](https://github.com/PJendritza/mxbiflow/commit/8f6ea51fb4e5770495aa80b3d89f15be7341811b))
* ✨ add Dorset LID665v42 RFID detector implementation ([fa425e9](https://github.com/PJendritza/mxbiflow/commit/fa425e91e1cb93c07803f91f153765edbbf3a197))
* ✨ add Dorset LID665v42 RFID detector implementation ([b89a856](https://github.com/PJendritza/mxbiflow/commit/b89a8560036f0ef460105eb71674323905df73e2))
* ✨ add entry reward and session trial tracking ([f690bed](https://github.com/PJendritza/mxbiflow/commit/f690bed0ea5f948db5780cfbbdcdda185abe4943))
* ✨ add entry reward and session trial tracking ([ee323bd](https://github.com/PJendritza/mxbiflow/commit/ee323bd82705802c1f983038e3bf2281dee3d5be))
* ✨ add error handling for unknown animal names ([9078028](https://github.com/PJendritza/mxbiflow/commit/9078028a1a96717965f9c2bb525a36712e85ff71))
* ✨ add error handling for unknown animal names ([12d719f](https://github.com/PJendritza/mxbiflow/commit/12d719f184abb1157ea7749a5ec685164342af27))
* ✨ add RFID example script and hide cursor in full screen ([1ded4df](https://github.com/PJendritza/mxbiflow/commit/1ded4dfb2e495299f5e62d8c52f46b057bf51ff1))
* ✨ add screenshot capture functionality with mss dependency ([d4b52e9](https://github.com/PJendritza/mxbiflow/commit/d4b52e9f2fcac19a02f03928b67f52e70116f281))
* ✨ add screenshot capture functionality with mss dependency ([f42dd1e](https://github.com/PJendritza/mxbiflow/commit/f42dd1e5ba0927c65089f24426f3f5d01e1fc7f0))
* ✨ add serial error handling and frame parser error recording ([2797584](https://github.com/PJendritza/mxbiflow/commit/2797584bf9cab4cbd57bd86a6eea45185c889a53))
* ✨ add serial error handling and frame parser error recording ([d37b2ac](https://github.com/PJendritza/mxbiflow/commit/d37b2ac9389b3db9940240791407aa3f5f8f2c6e))
* ✨ add session time tracking and difficulty adjustment ([0f1b117](https://github.com/PJendritza/mxbiflow/commit/0f1b11724ab964bddb4648e5b125ca39788216ce))
* ✨ add session time tracking and difficulty adjustment ([4e29073](https://github.com/PJendritza/mxbiflow/commit/4e290734bd31704391f4664a8a64aa16779fc24e))
* ✨ add standard reward stimulus flow ([2446706](https://github.com/PJendritza/mxbiflow/commit/2446706b0de8c9805971616f5e8e7aabeba064c1))
* ✨ add standard reward stimulus flow ([5b575d3](https://github.com/PJendritza/mxbiflow/commit/5b575d316548a6462915a4104e7195d418126c4a))
* ✨ add state transition logging with reason tracking ([3787990](https://github.com/PJendritza/mxbiflow/commit/378799072ee9bbfdaeef130e2e998dfb0220fa4a))
* ✨ add TWOAC size reduction stage implementation ([c716f55](https://github.com/PJendritza/mxbiflow/commit/c716f5519c6f4dedb98a9f3e8c7b11197bfb6fb8))
* ✨ adjust reward intervals and add new level 12 ([0a497e7](https://github.com/PJendritza/mxbiflow/commit/0a497e79e49adf98a7d7bb8c3a6f7121fb207e0b))
* ✨ sync data to samba serve by rsync ([a22c273](https://github.com/PJendritza/mxbiflow/commit/a22c2739023783c0bcff1bb4199c19bf0306e870))
* ✨ update animal IDs and add new animals to session ([dd1d025](https://github.com/PJendritza/mxbiflow/commit/dd1d025ad81ec5cb62b2e77f31724fbadacfea97))
* ✨ update animal IDs and add new animals to session ([a8d6f88](https://github.com/PJendritza/mxbiflow/commit/a8d6f88c153c631620373f4df61d9873f81885fc))
* 🎨 add gitmoji support in renovate config ([8998c99](https://github.com/PJendritza/mxbiflow/commit/8998c999aa419957d9fbeb667c843251917ecc9d))
* 🎨 add gitmoji support in renovate config ([6ba8888](https://github.com/PJendritza/mxbiflow/commit/6ba88885c496d951bc5b44ebe170fec3f46d2556))
* 🔥 remove platform enum from factory ([#24](https://github.com/PJendritza/mxbiflow/issues/24)) ([1980d13](https://github.com/PJendritza/mxbiflow/commit/1980d135075c071edc2842c87bbfaf880f3b24db))
* add animal mapping and unknown animal handling ([b72243c](https://github.com/PJendritza/mxbiflow/commit/b72243cf7bfa0e5a0750a4c17214932e5788f5d5))
* Add cross-modal task model and UI definitions ([28adb7a](https://github.com/PJendritza/mxbiflow/commit/28adb7ae0012d150942b88b5160c631c768ff8dd))
* add default module exports for Habituarion and IDLE ([7b94346](https://github.com/PJendritza/mxbiflow/commit/7b9434618cc8d97141b8d9e31af49f2345173c98))
* add detector bridge for event handling ([0b7b84c](https://github.com/PJendritza/mxbiflow/commit/0b7b84c18316576f82eabbdbce61f3c5f4e59193))
* Add example subjects from cross-modal example data ([3e0edb4](https://github.com/PJendritza/mxbiflow/commit/3e0edb49d60ff4f43c4d1951357f5fd9bb5b66f9))
* add game engine and scene management ([31caff4](https://github.com/PJendritza/mxbiflow/commit/31caff419a6f6b4c69b31dc7f62f9d3309fc6d6b))
* add habituation scene with config and reward system ([53cd817](https://github.com/PJendritza/mxbiflow/commit/53cd817927ff90f71c20572cfdbe4c65c29915b0))
* add idle scene with asset loading and rendering ([7be71cf](https://github.com/PJendritza/mxbiflow/commit/7be71cf1e7ee36b012bd567a602159feedfe17f3))
* add mxbi, options, and session config files ([3ae3577](https://github.com/PJendritza/mxbiflow/commit/3ae3577e740081e81f2a65e687b781fc5a9fbf59))
* add MXBIFlow class with session and timer ([06ea7be](https://github.com/PJendritza/mxbiflow/commit/06ea7bebb0575f91033b0b6e921001072bb0f344))
* add MXBIFlow exports to __init__.py ([dfc2e5e](https://github.com/PJendritza/mxbiflow/commit/dfc2e5e5c0d5dbdb299e6a61aa1cf10544b10a99))
* add new detector cards and reorganize imports ([187ec78](https://github.com/PJendritza/mxbiflow/commit/187ec7810986f1805552976e4a0c713b643e2dd8))
* add numpy and pyaudio dependencies ([00d3f29](https://github.com/PJendritza/mxbiflow/commit/00d3f29093a58defb143dc1cb2f7455c512d0434))
* Add option of cross-modal recognition task ([e884c9c](https://github.com/PJendritza/mxbiflow/commit/e884c9cff29ab6ba94dca181acf363328924d530))
* add PySide6 UI components for MXBI configuration ([0e9021c](https://github.com/PJendritza/mxbiflow/commit/0e9021c51921bca8262235ed155467db23468275))
* add rejected signal to panels and wizard ([cb3fb98](https://github.com/PJendritza/mxbiflow/commit/cb3fb9842a572a3bb1329a541f2fe26864bcc91c))
* add running state control to size reduction stage ([152455b](https://github.com/PJendritza/mxbiflow/commit/152455bec1c6f11430fc71e5e955234f2963a28a))
* add scene manager and reorganize scene protocol ([0d47593](https://github.com/PJendritza/mxbiflow/commit/0d475931f7698ca19e262cd126b392c0975e3236))
* add scheduler for event handling and scene management ([173b2ae](https://github.com/PJendritza/mxbiflow/commit/173b2ae438dc8264b841f2cd4dc4c285ae22cafc))
* Add selection of trials file and media dir to launch panel ([e8afd00](https://github.com/PJendritza/mxbiflow/commit/e8afd005ecf21ee86a18fd05ef3eaa989584bd8d))
* add session model and screen size configuration ([4943330](https://github.com/PJendritza/mxbiflow/commit/4943330b5fe15898540f4c040ad7f989d02da71f))
* add size reduction stage and target sprite ([f0e98eb](https://github.com/PJendritza/mxbiflow/commit/f0e98eb6d75634db29a71580943de8f282ced1be))
* add stage configuration to AnimalCard ([5105dd0](https://github.com/PJendritza/mxbiflow/commit/5105dd076030a9b8c4499e5cf815400f29c3d8a4))
* add STAGE_PATH constant for stage.json ([ae25ed4](https://github.com/PJendritza/mxbiflow/commit/ae25ed45a31c8056e89d31e7a032c901da234dce))
* Add wave file playing ([d1187f8](https://github.com/PJendritza/mxbiflow/commit/d1187f8a8a886b8f1130ec3b799c94abc1410512))
* **api:** :sparkles: expose experiment scaffold API ([#110](https://github.com/PJendritza/mxbiflow/issues/110)) ([e1f4a9c](https://github.com/PJendritza/mxbiflow/commit/e1f4a9c8e3131a54ca23ef6b0566dec92652de1c))
* **assets:** :sparkles: add ImageSprite and reorganize asset directories ([#118](https://github.com/PJendritza/mxbiflow/issues/118)) ([52b3fcb](https://github.com/PJendritza/mxbiflow/commit/52b3fcbe5a653b8a57dff02010eee6e25f35ca04))
* **assets:** :sparkles: add pygame experiment widgets ([#98](https://github.com/PJendritza/mxbiflow/issues/98)) ([6fc9897](https://github.com/PJendritza/mxbiflow/commit/6fc98978b0f313f1494050c45bb76cb4e11abe6c))
* **assets:** ✨ support configurable background colors ([#122](https://github.com/PJendritza/mxbiflow/issues/122)) ([aa49d93](https://github.com/PJendritza/mxbiflow/commit/aa49d93e67ff35360b4e06cc46944d1ca949c037))
* **audioplayer:** :sparkles: add soundfile-based wav loading and reusable playback ([#38](https://github.com/PJendritza/mxbiflow/issues/38)) ([7fe1224](https://github.com/PJendritza/mxbiflow/commit/7fe122464406866707e1a12bdc259f87fd132b25))
* **backup:** :sparkles: add backup task monitoring and progress UI ([#100](https://github.com/PJendritza/mxbiflow/issues/100)) ([714647d](https://github.com/PJendritza/mxbiflow/commit/714647d4ebb563b3270aeca01a3215a9baed87e2))
* **backup:** :sparkles: add session backup workflow ([#126](https://github.com/PJendritza/mxbiflow/issues/126)) ([5b36c95](https://github.com/PJendritza/mxbiflow/commit/5b36c953de7eb3432f997c2f174da6eed93a2bb0))
* Cache trial store to not repeat trials ([adb4141](https://github.com/PJendritza/mxbiflow/commit/adb414138533773907351afcd168abbff52644b5))
* **crash-report:** :sparkles: add crash report delivery ([#129](https://github.com/PJendritza/mxbiflow/issues/129)) ([928b67f](https://github.com/PJendritza/mxbiflow/commit/928b67ffd54540184ec6bdf29f63396b83a6d8e2))
* **crash-report:** :sparkles: add crash report generation with email notification ([#121](https://github.com/PJendritza/mxbiflow/issues/121)) ([81f6221](https://github.com/PJendritza/mxbiflow/commit/81f62216842f9400c65d00c642fe0557ec864581))
* **cross-modal:** add configurable visual/audio settings, preload st… ([a49d92b](https://github.com/PJendritza/mxbiflow/commit/a49d92ba31f787a1d8944b4d493371c122ee7b8c))
* **cross-modal:** add configurable visual/audio settings, preload stimuli, and rotate/resize images [#2](https://github.com/PJendritza/mxbiflow/issues/2) ([5d2ee84](https://github.com/PJendritza/mxbiflow/commit/5d2ee840762205884ff18b52c8903b7c2cbb4f35))
* **detector:** :sparkles: add poll intervals and rfid timeout configs ([2e9b265](https://github.com/PJendritza/mxbiflow/commit/2e9b2650935a7b4b7d2dbd209e8209461b62b9a7))
* **detector:** :sparkles: add poll_interval and rfid_timeout to FusionContinuousDetector ([#46](https://github.com/PJendritza/mxbiflow/issues/46)) ([50ea757](https://github.com/PJendritza/mxbiflow/commit/50ea757d943c97f84a7d05ee31bdd98e845af67e))
* **detector:** :sparkles: identify unknown animals after RFID timeout ([#156](https://github.com/PJendritza/mxbiflow/issues/156)) ([cddd5aa](https://github.com/PJendritza/mxbiflow/commit/cddd5aa86d287f4d3c83c6e0fbafff1f2a06a3d9))
* **detector:** ✨ add configurable beam-break filtering ([33c840f](https://github.com/PJendritza/mxbiflow/commit/33c840f9f277e02979bc4184bb73c823f6afa943))
* **driver:** :sparkles: integrate pymxbi hardware layer ([936d481](https://github.com/PJendritza/mxbiflow/commit/936d481cf76d9bc5ba5487c425c05f3869fc0f47))
* **driver:** ✨ integrate pymxbi hardware layer ([15522d0](https://github.com/PJendritza/mxbiflow/commit/15522d0ba587681fef6e3b6486c4d9c1400a0aaf))
* Expand mock detector to simulate whichever animal ([7e65084](https://github.com/PJendritza/mxbiflow/commit/7e6508456cbbef09fc3f0e7e25c07ad7f1a74f18))
* **eyetracker:** :sparkles: add py-mx-eye eyetracker driver ([#149](https://github.com/PJendritza/mxbiflow/issues/149)) ([eb8dc7a](https://github.com/PJendritza/mxbiflow/commit/eb8dc7ac90b95abc328b8707283339b9e4991e7d))
* **gameloop:** :sparkles: add configurable max fps at initialization ([#79](https://github.com/PJendritza/mxbiflow/issues/79)) ([34c83aa](https://github.com/PJendritza/mxbiflow/commit/34c83aa40c7fac99ccf6c3304e33e2a831c2b91b))
* **gameloop:** :sparkles: add manual level and stage navigation shortcuts ([#133](https://github.com/PJendritza/mxbiflow/issues/133)) ([44e962b](https://github.com/PJendritza/mxbiflow/commit/44e962bb86cacf66c286222146cfc816735e60a0))
* **gameloop:** :sparkles: add screenshot capture hotkey ([#66](https://github.com/PJendritza/mxbiflow/issues/66)) ([e88a820](https://github.com/PJendritza/mxbiflow/commit/e88a820295c5c28d8b3e2a0adf7bb4dd0d36807e))
* **gameloop:** :sparkles: add settlement module with rate and count logic ([#9](https://github.com/PJendritza/mxbiflow/issues/9)) ([590d746](https://github.com/PJendritza/mxbiflow/commit/590d746cf011012728b0450e4117881072409b33))
* **gameloop:** :sparkles: centralize keyboard shortcuts ([#132](https://github.com/PJendritza/mxbiflow/issues/132)) ([8c210e0](https://github.com/PJendritza/mxbiflow/commit/8c210e086c2d103abea9bbf53faaab9190c6656e))
* Have trials file per animal and relative resolution of media dir ([e9f44fd](https://github.com/PJendritza/mxbiflow/commit/e9f44fdd672a835458458553728e6c0e8ac35b38))
* **idle:** :sparkles: add manual control buttons ([#145](https://github.com/PJendritza/mxbiflow/issues/145)) ([91113f7](https://github.com/PJendritza/mxbiflow/commit/91113f7e55f324a2a4ab09b6a85c058993b21f08))
* **infra:** :sparkles: add post-processing module for session summary ([#51](https://github.com/PJendritza/mxbiflow/issues/51)) ([a91b78d](https://github.com/PJendritza/mxbiflow/commit/a91b78d92fc459945ee23a33d2ccb951d2344960))
* integrate detector events and refactor scene management ([90e09b9](https://github.com/PJendritza/mxbiflow/commit/90e09b9e4cb0dd80f67f25d1a47a8e6c86fe0967))
* Log results in CSV format as well ([d6f64d6](https://github.com/PJendritza/mxbiflow/commit/d6f64d618f4f0cc732a7f716f7672d9484423aea))
* **logging:** :sparkles: add default log file handling ([#130](https://github.com/PJendritza/mxbiflow/issues/130)) ([4fb79f5](https://github.com/PJendritza/mxbiflow/commit/4fb79f57a4a47b8c2c6ad5555a13ed7a063ad1e0))
* **models:** :sparkles: add context management to StageState ([#7](https://github.com/PJendritza/mxbiflow/issues/7)) ([ff7d6f7](https://github.com/PJendritza/mxbiflow/commit/ff7d6f746761f7cfa224f007c4bf815128001563))
* **models:** :sparkles: add initial/final stage serialization to Animal ([#89](https://github.com/PJendritza/mxbiflow/issues/89)) ([7ed5e49](https://github.com/PJendritza/mxbiflow/commit/7ed5e49a30c8751f487abd15f7ca3d7c7375ec43))
* **post-processing:** :sparkles: add sequential session post-processing ([#128](https://github.com/PJendritza/mxbiflow/issues/128)) ([6a7fb18](https://github.com/PJendritza/mxbiflow/commit/6a7fb182a2d37309e1d49a8a641645a2e72beaae))
* refactor animal models and add mxbi models ([49e9e27](https://github.com/PJendritza/mxbiflow/commit/49e9e276b8023969d76dae3ccf7fb7bbc63b13f7))
* refactor Animals container to use name keys with RFID migration ([32e9607](https://github.com/PJendritza/mxbiflow/commit/32e96073a14ecdf88abc9f4743d8fe3ba7c69c64))
* refactor experiment UI with config groups and animal cards ([54d7ce0](https://github.com/PJendritza/mxbiflow/commit/54d7ce0eb1b80839af1d1b2063add0d84ce8fbfc))
* **report:** :sparkles: add shared image section renderer ([e26d834](https://github.com/PJendritza/mxbiflow/commit/e26d83410f1a97dc3dc691b09368ffdb3eee4ce5))
* **scene:** :sparkles: spport set default, fallback scene ([630e198](https://github.com/PJendritza/mxbiflow/commit/630e19886e2f2263752cb3b31405329561869800))
* **scene:** :sparkles: standardize scene names as snake case ([#131](https://github.com/PJendritza/mxbiflow/issues/131)) ([26353c4](https://github.com/PJendritza/mxbiflow/commit/26353c45a1a95e5f9f6f1c5c22907d768308d67b))
* **scene:** add scene selection UI and config fields ([6cea878](https://github.com/PJendritza/mxbiflow/commit/6cea8784897100e6404512bb35f147bbcbe9f381))
* **scene:** apply session scene config to game ([0a559ad](https://github.com/PJendritza/mxbiflow/commit/0a559ad7b1d71ddda9f6eec8ee08ddc7584b9d06))
* **session:** :sparkles: add email send state storage ([2cfadf9](https://github.com/PJendritza/mxbiflow/commit/2cfadf9cef81736f191d56760f9f3c7eaa2cc39f))
* **session:** :sparkles: add session configuration persistence ([#49](https://github.com/PJendritza/mxbiflow/issues/49)) ([97c5723](https://github.com/PJendritza/mxbiflow/commit/97c5723de69b2c7adfd0124dcd8217f6dda510c5))
* **session:** :sparkles: track stage data paths ([#123](https://github.com/PJendritza/mxbiflow/issues/123)) ([471383d](https://github.com/PJendritza/mxbiflow/commit/471383dea509f8dfdfa211b26a28c2c17b81021a))
* **ui:** :sparkles: add auto-accept countdown timer to config panels ([#43](https://github.com/PJendritza/mxbiflow/issues/43)) ([a0e479d](https://github.com/PJendritza/mxbiflow/commit/a0e479d793270244902575a4856a9657c9ac68b9))
* **ui:** :sparkles: add send_email and sync_data checkboxes ([#64](https://github.com/PJendritza/mxbiflow/issues/64)) ([f47fc60](https://github.com/PJendritza/mxbiflow/commit/f47fc603fc39095a3f2fe9798bc9fcce450124da))
* **ui:** :sparkles: add session summary panel ([#113](https://github.com/PJendritza/mxbiflow/issues/113)) ([7506f4e](https://github.com/PJendritza/mxbiflow/commit/7506f4e19a5f911aebdcfec61e7d2d08f19ce2ea))
* **ui:** ✨ run companion tasks in backup panel ([#124](https://github.com/PJendritza/mxbiflow/issues/124)) ([325af5e](https://github.com/PJendritza/mxbiflow/commit/325af5e2a0c27ef48223dbfb60e901774d554f4b))
* **ui:** 🎨 add fullscreen and hide cursor options to session config ([19df3c2](https://github.com/PJendritza/mxbiflow/commit/19df3c2d5b845c4431c90c451603abcfe132b081))
* **ui:** 🔥 remove platform selection from BaseConfig ([#21](https://github.com/PJendritza/mxbiflow/issues/21)) ([dad8906](https://github.com/PJendritza/mxbiflow/commit/dad89066e5e173e3e912c21ecc69d2304f7e3e6b))


### Bug Fixes

* :ambulance: Fix minor bugs in the raspberryPi environment ([519036c](https://github.com/PJendritza/mxbiflow/commit/519036ce5fd9af80ed32ccf83e084c4fff813098))
* :ambulance: fix pumpfactory ([d066e18](https://github.com/PJendritza/mxbiflow/commit/d066e189b590b27d941693d64f9c437190975df9))
* :ambulance: fix pumpfactory ([204eb00](https://github.com/PJendritza/mxbiflow/commit/204eb00ccb1ee956fa510fdbf6461cf4facbe05d))
* :bug: fix amixer availability check with fallback mock output ([#18](https://github.com/PJendritza/mxbiflow/issues/18)) ([31b18db](https://github.com/PJendritza/mxbiflow/commit/31b18dbe29473a4dde805f60de95ddb5677aee1e))
* :bug: Fix the issue where the idle task is sometimes not cleaned up properly ([631cd9b](https://github.com/PJendritza/mxbiflow/commit/631cd9b8486b211d698893065bbdc1b74186bedc))
* :bug: Fix the issue where the idle task is sometimes not cleaned up properly ([1b154dd](https://github.com/PJendritza/mxbiflow/commit/1b154ddd6e5cf7b20c7b64fbf3dcb7e0975a7942))
* :bug: fixed the default export issue ([2fb8f4d](https://github.com/PJendritza/mxbiflow/commit/2fb8f4d0a339dfd5250c6492fe088479b8730d96))
* :bug: fixed the issue of directly accessing the state machine instead of using thread-safe methods ([fbdfe35](https://github.com/PJendritza/mxbiflow/commit/fbdfe35a16f22934ef597cedf35ac01cd408f45f))
* :bug: Fixed the issue of incorrectly importing Logger ([656d271](https://github.com/PJendritza/mxbiflow/commit/656d2710b0e12d9541d29ba0cccc8236b4e333bc))
* :bug: fixed the issue of using expired RFID tags ([b89a070](https://github.com/PJendritza/mxbiflow/commit/b89a070438ef2bb58049940053dba4c7ed29ed8e))
* :bug: Now start to actively maintain the animal stay status ([20507d8](https://github.com/PJendritza/mxbiflow/commit/20507d887931048bcafc0eacb6b95bac9f057b30))
* :bug: Now start to actively maintain the animal stay status ([94f8512](https://github.com/PJendritza/mxbiflow/commit/94f8512f558b059d8381d53d4ac49c6c4f2036d6))
* :bug: register IDLE scene in SceneManager initialization ([6507ca3](https://github.com/PJendritza/mxbiflow/commit/6507ca34dd95ff12c3a3a320fb93077195e4ff01))
* :wrench: correct GitHub workflows directory path ([2f4e9a2](https://github.com/PJendritza/mxbiflow/commit/2f4e9a2731275c7d855ee9d4a6352c2257cba840))
* 🐛 adjust difficulty threshold in habituation config ([215d257](https://github.com/PJendritza/mxbiflow/commit/215d25756fa04984a9dd8a66b136f2d0018c2a44))
* 🐛 comment out apple image display in idle scene ([a220249](https://github.com/PJendritza/mxbiflow/commit/a220249de8e977a27087809592c27c580106979f))
* 🐛 comment out apple image display in idle scene ([1d2cb50](https://github.com/PJendritza/mxbiflow/commit/1d2cb50baff43d5afd9a8c3873aa4093366a82c6))
* 🐛 fix screen size selection to BaseConfig UI component ([7e016fd](https://github.com/PJendritza/mxbiflow/commit/7e016fdd61604f03617cac2406f5534355c15078))
* 🐛 improve screen size selection in BaseConfig ([#15](https://github.com/PJendritza/mxbiflow/issues/15)) ([0d5c5f7](https://github.com/PJendritza/mxbiflow/commit/0d5c5f7155ec3323029454a5bad135a6c9f3410f))
* **audioplayer:** :bug: align playback paths with supported formats ([#42](https://github.com/PJendritza/mxbiflow/issues/42)) ([38e5884](https://github.com/PJendritza/mxbiflow/commit/38e588480939e5e261e427923416f21fe29e71fe))
* **audioplayer:** migrate playback backend to sounddevice ([#44](https://github.com/PJendritza/mxbiflow/issues/44)) ([a358e9a](https://github.com/PJendritza/mxbiflow/commit/a358e9a09304b520c31a631f43051ab369b26987))
* change mxbi_id type from int to str ([#34](https://github.com/PJendritza/mxbiflow/issues/34)) ([4026233](https://github.com/PJendritza/mxbiflow/commit/4026233526d90ce3c65dde0a29cdd40012d01f2e))
* **ci:** use config-file instead of release-type for release-please ([#28](https://github.com/PJendritza/mxbiflow/issues/28)) ([abcf545](https://github.com/PJendritza/mxbiflow/commit/abcf54520d7d9b93351fd3be9e66417bcab2a3b3))
* **ci:** use config-file instead of release-type for release-please ([#28](https://github.com/PJendritza/mxbiflow/issues/28)) ([56c2153](https://github.com/PJendritza/mxbiflow/commit/56c2153f24f3979b3d1111944e9ed67fd3d92270))
* **core:** :bug: support cross-platform home paths ([#141](https://github.com/PJendritza/mxbiflow/issues/141)) ([97a8b2a](https://github.com/PJendritza/mxbiflow/commit/97a8b2a124531a33a08f41b9d9972f434de5fc0e))
* **deps:** ⬆️ update dependency pymotego to &gt;=0.1.4 ([#32](https://github.com/PJendritza/mxbiflow/issues/32)) ([9586007](https://github.com/PJendritza/mxbiflow/commit/9586007d3765053cb49bb52b6fab81021bf8902d))
* **deps:** ⬆️ update dependency pymotego to &gt;=0.1.5 ([#36](https://github.com/PJendritza/mxbiflow/issues/36)) ([3879e54](https://github.com/PJendritza/mxbiflow/commit/3879e54034bfdbbc5a41045754ed3852cf6e245a))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.1 ([#32](https://github.com/PJendritza/mxbiflow/issues/32)) ([f41aa2e](https://github.com/PJendritza/mxbiflow/commit/f41aa2e6453b56e9a58837fa8e32a2474c9e5491))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.2 ([#34](https://github.com/PJendritza/mxbiflow/issues/34)) ([9cd3f7f](https://github.com/PJendritza/mxbiflow/commit/9cd3f7fbe82799947d31164117d2eb0667499d00))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.3 ([#42](https://github.com/PJendritza/mxbiflow/issues/42)) ([e3a4c2b](https://github.com/PJendritza/mxbiflow/commit/e3a4c2bacc0a6adc22bd823b54a90ff224451efa))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.4 ([#55](https://github.com/PJendritza/mxbiflow/issues/55)) ([b158ad0](https://github.com/PJendritza/mxbiflow/commit/b158ad0094c3dc77fd840ad22bad8dbec73e40cf))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.5 ([#68](https://github.com/PJendritza/mxbiflow/issues/68)) ([717e1a0](https://github.com/PJendritza/mxbiflow/commit/717e1a0c572ea026a110b48ab6ceb1c8c1613404))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.6 ([#75](https://github.com/PJendritza/mxbiflow/issues/75)) ([f99c7bb](https://github.com/PJendritza/mxbiflow/commit/f99c7bbfd97d25e3368ab54d913dd300baa51c1c))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.7 ([#83](https://github.com/PJendritza/mxbiflow/issues/83)) ([300d678](https://github.com/PJendritza/mxbiflow/commit/300d678bf35def3dd2134c9ea786cd5e56aee6c9))
* **deps:** remove pyaudio dependency ([351d065](https://github.com/PJendritza/mxbiflow/commit/351d06531e9a0ced0a4640ca771355b8c7335a69))
* **detector:** 🐛 add mxbi initialization and cleanup in Game class ([#19](https://github.com/PJendritza/mxbiflow/issues/19)) ([6be6d72](https://github.com/PJendritza/mxbiflow/commit/6be6d72948942d807070fcb5cb68354f339242bd))
* **detector:** 🐛 fix the detector initialization process ([#20](https://github.com/PJendritza/mxbiflow/issues/20)) ([98458dd](https://github.com/PJendritza/mxbiflow/commit/98458dd49c35b28f2ec938ba278c1350642bf9c5))
* **detector:** 🐛 prevent duplicate thread initialization ([#22](https://github.com/PJendritza/mxbiflow/issues/22)) ([af6814a](https://github.com/PJendritza/mxbiflow/commit/af6814a156bd32e883e170052ff5360bead0ce8e))
* **eyetracker:** :alien: update py-mx-eye driver for the reworked SDK ([#153](https://github.com/PJendritza/mxbiflow/issues/153)) ([25371f0](https://github.com/PJendritza/mxbiflow/commit/25371f09a13bb5fb7d50b0cb0a315a3591e550ce))
* **eyetracker:** consume mx-eye gaze coordinates ([bd7b43b](https://github.com/PJendritza/mxbiflow/commit/bd7b43ba3066aaae41cdad4ce203b87dd6832375))
* improve detector fallback handling and pygame display lifecycle ([#81](https://github.com/PJendritza/mxbiflow/issues/81)) ([ea70f82](https://github.com/PJendritza/mxbiflow/commit/ea70f82bfe9bc0ea840ab6129b7d3fe7ceb56c46))
* **mxbi:** :bug: allow default MXBI config without backup root ids ([#137](https://github.com/PJendritza/mxbiflow/issues/137)) ([8885cbb](https://github.com/PJendritza/mxbiflow/commit/8885cbbf2614aac9e2f434725719fcec53de9353))
* refactor eventbus subscribe logic to prevent duplicate handlers ([03a0cbe](https://github.com/PJendritza/mxbiflow/commit/03a0cbe03c24e3d82b54397a0275b898928909c0))
* remove unused mxbi and session config files ([51df63c](https://github.com/PJendritza/mxbiflow/commit/51df63c80dcf7a068dce71b2579840ac7e285d17))
* **renovate:** add bump rangeStrategy for pymotego ([#30](https://github.com/PJendritza/mxbiflow/issues/30)) ([53bc73c](https://github.com/PJendritza/mxbiflow/commit/53bc73c95c38e2b3692c68b416bed6c1b0d55236))
* **renovate:** add bump rangeStrategy for pymxbi ([#30](https://github.com/PJendritza/mxbiflow/issues/30)) ([5745e04](https://github.com/PJendritza/mxbiflow/commit/5745e0419c57925ca904b736545a379af5981bf5))
* reset current_result after reading in DorsetLID665v42 ([8bfe9c5](https://github.com/PJendritza/mxbiflow/commit/8bfe9c56b1f2d183e45c18f25b6e8d5cd7db5aaa))
* **scene:** :art: rotate apple assets 90 degrees clockwise in idle scene ([#44](https://github.com/PJendritza/mxbiflow/issues/44)) ([14f5eeb](https://github.com/PJendritza/mxbiflow/commit/14f5eeb4fd4be30308f2b1bb81c66945baac8f75))
* **scheduler:** :bug: route detector fallback events to configured scenes ([#76](https://github.com/PJendritza/mxbiflow/issues/76)) ([81fdc13](https://github.com/PJendritza/mxbiflow/commit/81fdc13c38d0d3e110743d03cd3198bcc862b21a))
* **session:** :bug: allocate session_id only when session starts ([#65](https://github.com/PJendritza/mxbiflow/issues/65)) ([7f90e72](https://github.com/PJendritza/mxbiflow/commit/7f90e7297f49a99a760ec94a5e3844771d4b5544))
* **session:** :bug: fix daily rollover for session data directories ([#73](https://github.com/PJendritza/mxbiflow/issues/73)) ([001a342](https://github.com/PJendritza/mxbiflow/commit/001a342cdb87267801110c0320f90cfc022724c5))
* **session:** :bug: persist animal training progress ([#143](https://github.com/PJendritza/mxbiflow/issues/143)) ([6265ff4](https://github.com/PJendritza/mxbiflow/commit/6265ff454beccef3f5d8c0c68fe72f482c028da8))
* **ui:** :bug: fix experimenter persistence in non-editable combobox ([#61](https://github.com/PJendritza/mxbiflow/issues/61)) ([4d3cc78](https://github.com/PJendritza/mxbiflow/commit/4d3cc7802e222b9d7d71ac7dc69f9f6642e52048))
* **ui:** :bug: remove unnecessary str() conversion for mxbi_id ([#40](https://github.com/PJendritza/mxbiflow/issues/40)) ([e966ce3](https://github.com/PJendritza/mxbiflow/commit/e966ce3c906eb0d88cbf305fb093a3733fe76e42))
* **ui:** make countdown controls explicit ([#112](https://github.com/PJendritza/mxbiflow/issues/112)) ([8e0e019](https://github.com/PJendritza/mxbiflow/commit/8e0e019fc37a5b4ed8f3da57f9deeb29e4bb2d59))
* **ui:** make panel countdowns independent ([#104](https://github.com/PJendritza/mxbiflow/issues/104)) ([e833836](https://github.com/PJendritza/mxbiflow/commit/e8338368a52921a941026f626e263e7b5d42050b))
* **ui:** optimize column stretch in devices layout ([2731637](https://github.com/PJendritza/mxbiflow/commit/27316370707096983cce12e538c1b2791030691d))
* update RFID port and baudrate configuration ([ccb8950](https://github.com/PJendritza/mxbiflow/commit/ccb895058ce912a5668080e9f6abd28e8dc8583e))


### Documentation

* :bulb: add comprehensive docstrings to detector module ([38883ae](https://github.com/PJendritza/mxbiflow/commit/38883ae1354d33f6548f63a70252adadd6895857))
* :bulb: standardize docstrings and improve documentation ([e99c637](https://github.com/PJendritza/mxbiflow/commit/e99c63764e1e89cb9c99423b871a6fa4face8b37))
* :memo: add comprehensive API documentation ([00a3465](https://github.com/PJendritza/mxbiflow/commit/00a34653dd81a2262978c0bf56049fcee6129746))
* :memo: add data sync documentation ([e214fbb](https://github.com/PJendritza/mxbiflow/commit/e214fbbfc7932364b7cdd1af5a14a952c8b4e593))
* :memo: update project description for pymxbi ([14168d0](https://github.com/PJendritza/mxbiflow/commit/14168d083d1f9a9bda1537ff5ab7658e41e73ed0))
* :wrench: update description and remove workspace config ([488c0de](https://github.com/PJendritza/mxbiflow/commit/488c0de9e4dbee3d665e514cb0c82339da5818f2))
* 📝 update README with new architecture and usage ([9684454](https://github.com/PJendritza/mxbiflow/commit/96844549e710768692924448511719139a9aaa86))

## [0.3.26](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.25...v0.3.26) (2026-10-06)


### Features

* **detector:** :sparkles: identify unknown animals after RFID timeout ([#156](https://github.com/CHiPmxbi/mxbiflow/issues/156)) ([cddd5aa](https://github.com/CHiPmxbi/mxbiflow/commit/cddd5aa86d287f4d3c83c6e0fbafff1f2a06a3d9))

## [0.3.25](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.24...v0.3.25) (2026-09-30)


### Bug Fixes

* **eyetracker:** :alien: update py-mx-eye driver for the reworked SDK ([#153](https://github.com/CHiPmxbi/mxbiflow/issues/153)) ([25371f0](https://github.com/CHiPmxbi/mxbiflow/commit/25371f09a13bb5fb7d50b0cb0a315a3591e550ce))

## [0.3.24](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.23...v0.3.24) (2026-09-28)


### Features

* **eyetracker:** :sparkles: add py-mx-eye eyetracker driver ([#149](https://github.com/CHiPmxbi/mxbiflow/issues/149)) ([eb8dc7a](https://github.com/CHiPmxbi/mxbiflow/commit/eb8dc7ac90b95abc328b8707283339b9e4991e7d))

## [0.3.23](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.22...v0.3.23) (2026-08-27)


### Features

* **idle:** :sparkles: add manual control buttons ([#145](https://github.com/CHiPmxbi/mxbiflow/issues/145)) ([91113f7](https://github.com/CHiPmxbi/mxbiflow/commit/91113f7e55f324a2a4ab09b6a85c058993b21f08))

## [0.3.22](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.21...v0.3.22) (2026-08-27)


### Bug Fixes

* **session:** :bug: persist animal training progress ([#143](https://github.com/CHiPmxbi/mxbiflow/issues/143)) ([6265ff4](https://github.com/CHiPmxbi/mxbiflow/commit/6265ff454beccef3f5d8c0c68fe72f482c028da8))

## [0.3.21](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.20...v0.3.21) (2026-08-21)


### Bug Fixes

* **core:** :bug: support cross-platform home paths ([#141](https://github.com/CHiPmxbi/mxbiflow/issues/141)) ([97a8b2a](https://github.com/CHiPmxbi/mxbiflow/commit/97a8b2a124531a33a08f41b9d9972f434de5fc0e))

## [0.3.20](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.19...v0.3.20) (2026-08-21)


### Features

* **detector:** ✨ add configurable beam-break filtering ([33c840f](https://github.com/CHiPmxbi/mxbiflow/commit/33c840f9f277e02979bc4184bb73c823f6afa943))

## [0.3.19](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.18...v0.3.19) (2026-08-20)


### Bug Fixes

* **mxbi:** :bug: allow default MXBI config without backup root ids ([#137](https://github.com/CHiPmxbi/mxbiflow/issues/137)) ([8885cbb](https://github.com/CHiPmxbi/mxbiflow/commit/8885cbbf2614aac9e2f434725719fcec53de9353))

## [0.3.18](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.17...v0.3.18) (2026-08-19)


### Features

* **backup:** :sparkles: add session backup workflow ([#126](https://github.com/CHiPmxbi/mxbiflow/issues/126)) ([5b36c95](https://github.com/CHiPmxbi/mxbiflow/commit/5b36c953de7eb3432f997c2f174da6eed93a2bb0))
* **crash-report:** :sparkles: add crash report delivery ([#129](https://github.com/CHiPmxbi/mxbiflow/issues/129)) ([928b67f](https://github.com/CHiPmxbi/mxbiflow/commit/928b67ffd54540184ec6bdf29f63396b83a6d8e2))
* **gameloop:** :sparkles: add manual level and stage navigation shortcuts ([#133](https://github.com/CHiPmxbi/mxbiflow/issues/133)) ([44e962b](https://github.com/CHiPmxbi/mxbiflow/commit/44e962bb86cacf66c286222146cfc816735e60a0))
* **gameloop:** :sparkles: centralize keyboard shortcuts ([#132](https://github.com/CHiPmxbi/mxbiflow/issues/132)) ([8c210e0](https://github.com/CHiPmxbi/mxbiflow/commit/8c210e086c2d103abea9bbf53faaab9190c6656e))
* **logging:** :sparkles: add default log file handling ([#130](https://github.com/CHiPmxbi/mxbiflow/issues/130)) ([4fb79f5](https://github.com/CHiPmxbi/mxbiflow/commit/4fb79f57a4a47b8c2c6ad5555a13ed7a063ad1e0))
* **post-processing:** :sparkles: add sequential session post-processing ([#128](https://github.com/CHiPmxbi/mxbiflow/issues/128)) ([6a7fb18](https://github.com/CHiPmxbi/mxbiflow/commit/6a7fb182a2d37309e1d49a8a641645a2e72beaae))
* **scene:** :sparkles: standardize scene names as snake case ([#131](https://github.com/CHiPmxbi/mxbiflow/issues/131)) ([26353c4](https://github.com/CHiPmxbi/mxbiflow/commit/26353c45a1a95e5f9f6f1c5c22907d768308d67b))

## [0.3.17](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.16...v0.3.17) (2026-08-05)


### Features

* **api:** :sparkles: expose experiment scaffold API ([#110](https://github.com/CHiPmxbi/mxbiflow/issues/110)) ([e1f4a9c](https://github.com/CHiPmxbi/mxbiflow/commit/e1f4a9c8e3131a54ca23ef6b0566dec92652de1c))
* **assets:** :sparkles: add ImageSprite and reorganize asset directories ([#118](https://github.com/CHiPmxbi/mxbiflow/issues/118)) ([52b3fcb](https://github.com/CHiPmxbi/mxbiflow/commit/52b3fcbe5a653b8a57dff02010eee6e25f35ca04))
* **assets:** :sparkles: add pygame experiment widgets ([#98](https://github.com/CHiPmxbi/mxbiflow/issues/98)) ([6fc9897](https://github.com/CHiPmxbi/mxbiflow/commit/6fc98978b0f313f1494050c45bb76cb4e11abe6c))
* **assets:** ✨ support configurable background colors ([#122](https://github.com/CHiPmxbi/mxbiflow/issues/122)) ([aa49d93](https://github.com/CHiPmxbi/mxbiflow/commit/aa49d93e67ff35360b4e06cc46944d1ca949c037))
* **backup:** :sparkles: add backup task monitoring and progress UI ([#100](https://github.com/CHiPmxbi/mxbiflow/issues/100)) ([714647d](https://github.com/CHiPmxbi/mxbiflow/commit/714647d4ebb563b3270aeca01a3215a9baed87e2))
* **crash-report:** :sparkles: add crash report generation with email notification ([#121](https://github.com/CHiPmxbi/mxbiflow/issues/121)) ([81f6221](https://github.com/CHiPmxbi/mxbiflow/commit/81f62216842f9400c65d00c642fe0557ec864581))
* **driver:** :sparkles: integrate pymxbi hardware layer ([936d481](https://github.com/CHiPmxbi/mxbiflow/commit/936d481cf76d9bc5ba5487c425c05f3869fc0f47))
* **driver:** ✨ integrate pymxbi hardware layer ([15522d0](https://github.com/CHiPmxbi/mxbiflow/commit/15522d0ba587681fef6e3b6486c4d9c1400a0aaf))
* **session:** :sparkles: track stage data paths ([#123](https://github.com/CHiPmxbi/mxbiflow/issues/123)) ([471383d](https://github.com/CHiPmxbi/mxbiflow/commit/471383dea509f8dfdfa211b26a28c2c17b81021a))
* **ui:** :sparkles: add session summary panel ([#113](https://github.com/CHiPmxbi/mxbiflow/issues/113)) ([7506f4e](https://github.com/CHiPmxbi/mxbiflow/commit/7506f4e19a5f911aebdcfec61e7d2d08f19ce2ea))
* **ui:** ✨ run companion tasks in backup panel ([#124](https://github.com/CHiPmxbi/mxbiflow/issues/124)) ([325af5e](https://github.com/CHiPmxbi/mxbiflow/commit/325af5e2a0c27ef48223dbfb60e901774d554f4b))


### Bug Fixes

* **ui:** make countdown controls explicit ([#112](https://github.com/CHiPmxbi/mxbiflow/issues/112)) ([8e0e019](https://github.com/CHiPmxbi/mxbiflow/commit/8e0e019fc37a5b4ed8f3da57f9deeb29e4bb2d59))
* **ui:** make panel countdowns independent ([#104](https://github.com/CHiPmxbi/mxbiflow/issues/104)) ([e833836](https://github.com/CHiPmxbi/mxbiflow/commit/e8338368a52921a941026f626e263e7b5d42050b))

## [0.3.16](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.15...v0.3.16) (2026-05-04)


### Features

* **models:** :sparkles: add initial/final stage serialization to Animal ([#89](https://github.com/CHiPmxbi/mxbiflow/issues/89)) ([7ed5e49](https://github.com/CHiPmxbi/mxbiflow/commit/7ed5e49a30c8751f487abd15f7ca3d7c7375ec43))

## [0.3.15](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.14...v0.3.15) (2026-04-14)


### Bug Fixes

* **deps:** remove pyaudio dependency ([351d065](https://github.com/CHiPmxbi/mxbiflow/commit/351d06531e9a0ced0a4640ca771355b8c7335a69))

## [0.3.14](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.13...v0.3.14) (2026-04-01)


### Bug Fixes

* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.7 ([#83](https://github.com/CHiPmxbi/mxbiflow/issues/83)) ([300d678](https://github.com/CHiPmxbi/mxbiflow/commit/300d678bf35def3dd2134c9ea786cd5e56aee6c9))
* improve detector fallback handling and pygame display lifecycle ([#81](https://github.com/CHiPmxbi/mxbiflow/issues/81)) ([ea70f82](https://github.com/CHiPmxbi/mxbiflow/commit/ea70f82bfe9bc0ea840ab6129b7d3fe7ceb56c46))

## [0.3.13](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.12...v0.3.13) (2026-03-31)


### Features

* **gameloop:** :sparkles: add configurable max fps at initialization ([#79](https://github.com/CHiPmxbi/mxbiflow/issues/79)) ([34c83aa](https://github.com/CHiPmxbi/mxbiflow/commit/34c83aa40c7fac99ccf6c3304e33e2a831c2b91b))


### Bug Fixes

* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.6 ([#75](https://github.com/CHiPmxbi/mxbiflow/issues/75)) ([f99c7bb](https://github.com/CHiPmxbi/mxbiflow/commit/f99c7bbfd97d25e3368ab54d913dd300baa51c1c))
* **scheduler:** :bug: route detector fallback events to configured scenes ([#76](https://github.com/CHiPmxbi/mxbiflow/issues/76)) ([81fdc13](https://github.com/CHiPmxbi/mxbiflow/commit/81fdc13c38d0d3e110743d03cd3198bcc862b21a))

## [0.3.12](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.11...v0.3.12) (2026-03-24)


### Bug Fixes

* **session:** :bug: fix daily rollover for session data directories ([#73](https://github.com/CHiPmxbi/mxbiflow/issues/73)) ([001a342](https://github.com/CHiPmxbi/mxbiflow/commit/001a342cdb87267801110c0320f90cfc022724c5))

## [0.3.11](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.10...v0.3.11) (2026-02-26)


### Features

* **report:** :sparkles: add shared image section renderer ([e26d834](https://github.com/CHiPmxbi/mxbiflow/commit/e26d83410f1a97dc3dc691b09368ffdb3eee4ce5))

## [0.3.10](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.9...v0.3.10) (2026-02-26)


### Bug Fixes

* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.5 ([#68](https://github.com/CHiPmxbi/mxbiflow/issues/68)) ([717e1a0](https://github.com/CHiPmxbi/mxbiflow/commit/717e1a0c572ea026a110b48ab6ceb1c8c1613404))

## [0.3.9](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.8...v0.3.9) (2026-02-26)


### Features

* **gameloop:** :sparkles: add screenshot capture hotkey ([#66](https://github.com/CHiPmxbi/mxbiflow/issues/66)) ([e88a820](https://github.com/CHiPmxbi/mxbiflow/commit/e88a820295c5c28d8b3e2a0adf7bb4dd0d36807e))

## [0.3.8](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.7...v0.3.8) (2026-02-19)


### Features

* **ui:** :sparkles: add send_email and sync_data checkboxes ([#64](https://github.com/CHiPmxbi/mxbiflow/issues/64)) ([f47fc60](https://github.com/CHiPmxbi/mxbiflow/commit/f47fc603fc39095a3f2fe9798bc9fcce450124da))


### Bug Fixes

* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.4 ([#55](https://github.com/CHiPmxbi/mxbiflow/issues/55)) ([b158ad0](https://github.com/CHiPmxbi/mxbiflow/commit/b158ad0094c3dc77fd840ad22bad8dbec73e40cf))
* **session:** :bug: allocate session_id only when session starts ([#65](https://github.com/CHiPmxbi/mxbiflow/issues/65)) ([7f90e72](https://github.com/CHiPmxbi/mxbiflow/commit/7f90e7297f49a99a760ec94a5e3844771d4b5544))
* **ui:** :bug: fix experimenter persistence in non-editable combobox ([#61](https://github.com/CHiPmxbi/mxbiflow/issues/61)) ([4d3cc78](https://github.com/CHiPmxbi/mxbiflow/commit/4d3cc7802e222b9d7d71ac7dc69f9f6642e52048))

## [0.3.7](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.6...v0.3.7) (2026-02-18)


### Features

* **session:** :sparkles: add email send state storage ([2cfadf9](https://github.com/CHiPmxbi/mxbiflow/commit/2cfadf9cef81736f191d56760f9f3c7eaa2cc39f))

## [0.3.6](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.5...v0.3.6) (2026-02-17)


### Features

* **infra:** :sparkles: add post-processing module for session summary ([#51](https://github.com/CHiPmxbi/mxbiflow/issues/51)) ([a91b78d](https://github.com/CHiPmxbi/mxbiflow/commit/a91b78d92fc459945ee23a33d2ccb951d2344960))

## [0.3.5](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.4...v0.3.5) (2026-02-17)


### Features

* **session:** :sparkles: add session configuration persistence ([#49](https://github.com/CHiPmxbi/mxbiflow/issues/49)) ([97c5723](https://github.com/CHiPmxbi/mxbiflow/commit/97c5723de69b2c7adfd0124dcd8217f6dda510c5))

## [0.3.4](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.3...v0.3.4) (2026-02-17)


### Bug Fixes

* **scene:** :art: rotate apple assets 90 degrees clockwise in idle scene ([#44](https://github.com/CHiPmxbi/mxbiflow/issues/44)) ([14f5eeb](https://github.com/CHiPmxbi/mxbiflow/commit/14f5eeb4fd4be30308f2b1bb81c66945baac8f75))

## [0.3.3](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.2...v0.3.3) (2026-02-17)


### Features

* **ui:** :sparkles: add auto-accept countdown timer to config panels ([#43](https://github.com/CHiPmxbi/mxbiflow/issues/43)) ([a0e479d](https://github.com/CHiPmxbi/mxbiflow/commit/a0e479d793270244902575a4856a9657c9ac68b9))


### Bug Fixes

* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.1 ([#32](https://github.com/CHiPmxbi/mxbiflow/issues/32)) ([f41aa2e](https://github.com/CHiPmxbi/mxbiflow/commit/f41aa2e6453b56e9a58837fa8e32a2474c9e5491))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.2 ([#34](https://github.com/CHiPmxbi/mxbiflow/issues/34)) ([9cd3f7f](https://github.com/CHiPmxbi/mxbiflow/commit/9cd3f7fbe82799947d31164117d2eb0667499d00))
* **deps:** ⬆️ update dependency pymxbi to &gt;=0.3.3 ([#42](https://github.com/CHiPmxbi/mxbiflow/issues/42)) ([e3a4c2b](https://github.com/CHiPmxbi/mxbiflow/commit/e3a4c2bacc0a6adc22bd823b54a90ff224451efa))
* **ui:** :bug: remove unnecessary str() conversion for mxbi_id ([#40](https://github.com/CHiPmxbi/mxbiflow/issues/40)) ([e966ce3](https://github.com/CHiPmxbi/mxbiflow/commit/e966ce3c906eb0d88cbf305fb093a3733fe76e42))

## [0.3.2](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.1...v0.3.2) (2026-02-17)


### Bug Fixes

* **renovate:** add bump rangeStrategy for pymxbi ([#30](https://github.com/CHiPmxbi/mxbiflow/issues/30)) ([5745e04](https://github.com/CHiPmxbi/mxbiflow/commit/5745e0419c57925ca904b736545a379af5981bf5))

## [0.3.1](https://github.com/CHiPmxbi/mxbiflow/compare/v0.3.0...v0.3.1) (2026-02-17)


### Features

* 🎨 add gitmoji support in renovate config ([8998c99](https://github.com/CHiPmxbi/mxbiflow/commit/8998c999aa419957d9fbeb667c843251917ecc9d))


### Bug Fixes

* **ci:** use config-file instead of release-type for release-please ([#28](https://github.com/CHiPmxbi/mxbiflow/issues/28)) ([abcf545](https://github.com/CHiPmxbi/mxbiflow/commit/abcf54520d7d9b93351fd3be9e66417bcab2a3b3))

## [0.3.0](https://github.com/CHiPmxbi/mxbiflow/compare/v0.2.0...v0.3.0) (2026-02-13)


### Features

* **ui:** 🎨 add fullscreen and hide cursor options to session config ([19df3c2](https://github.com/CHiPmxbi/mxbiflow/commit/19df3c2d5b845c4431c90c451603abcfe132b081))


### Bug Fixes

* **ui:** optimize column stretch in devices layout ([2731637](https://github.com/CHiPmxbi/mxbiflow/commit/27316370707096983cce12e538c1b2791030691d))

## [0.2.0](https://github.com/CHiPmxbi/mxbiflow/compare/v0.1.10...v0.2.0) (2026-02-13)


### Features

* **ui:** 🔥 remove platform selection from BaseConfig ([#21](https://github.com/CHiPmxbi/mxbiflow/issues/21)) ([dad8906](https://github.com/CHiPmxbi/mxbiflow/commit/dad89066e5e173e3e912c21ecc69d2304f7e3e6b))

## [0.1.10](https://github.com/CHiPmxbi/mxbiflow/compare/v0.1.9...v0.1.10) (2026-02-13)


### Bug Fixes

* **detector:** 🐛 add mxbi initialization and cleanup in Game class ([#19](https://github.com/CHiPmxbi/mxbiflow/issues/19)) ([6be6d72](https://github.com/CHiPmxbi/mxbiflow/commit/6be6d72948942d807070fcb5cb68354f339242bd))
