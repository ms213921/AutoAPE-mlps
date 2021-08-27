# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jin.kim@seculayer.com
# Powered by Seculayer © 2021 Service Model Team, R&D Center.

import json
from typing import Tuple

from mlps.common.Constants import Constants
from mlps.core.data.cnvrtr.functions.SpWCAbstract import SpWCAbstract


class FUSpWC(SpWCAbstract):
    @staticmethod
    def _load_special_word_dict() -> Tuple[dict, dict]:
        keyword_map_path = "{}/{}".format(Constants.DIR_RESOURCES_CNVRTR, "FU_keywords_map.json")
        f = open(keyword_map_path, "r")
        special_dict = json.loads(f.read())
        f.close()
        return special_dict, {}

    def processConvert(self, data):
        return self.apply(data)


if __name__ == '__main__':
    str_data_list = list()
    str_data_list.append("\" ? ? ^ ? ? ? ? ? ? ? = ? ? ? ? ? ? ? ? @ ? ? ? + ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? * : | ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ^ ? ? ! ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? [ ? ? ? ? ^ ; ? ? ? ? ? ? ? ? ' * ? ? ? ? $ ? ? ' ? ? ? # ) ? ? ? ? ? > ? ? = ? ? ? ? ? ? ? ? ? ? ? ? { ? ? ? ? | ? ? ? ? ? ? ? ? \" \" ? ? | ] ? ? ? ? ? ? | ? % ? ? ? ? ? ? ? ? ? ? \\ ? ? | @ ? ? ? ? ? ? ? ? \" \" ? ? ? ? ? ? ? ~ ? ? ? ? ? ? \u007f ? ? ? ? ? / ? ? ? ? ? = ? ? ? ? ? _ ? ? ? ? ? ? * ? ? ~ ? ? ? ? \u007f ? ? ? ? ? ? ? ? ? ; ? ? ? ? ? ? ? $ cmd ? ? ? ? ? ? ? ? ? ? ? ? ^ ? ? ? ? ? ? _ ? ? % ? ? @ ? ? ? ? ? ? ? ? ? ? > ; ? * / ? ? ? } ? ? ? ? ? ? ( ? ? ? ? ? ? \" \" ? ? ? ? ? ? ? ? ' ? ? # ? ? ? ? ? ? ) ? ? ? ? ) ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? } ? ` ^ ? ? ? ? ? ? ? } ? ? ? ? ? = & ? ? ? ? ? ? ? ? ? ? ? ? ? ? - ? + } ? ? ? ? ? ' * ' ? ? ? ) ? ? ? ? ? ? \\ ? ; ! ? . ? ? ? ? : ? ? ? ? ? ` ? ? ? ? \" \" ? ? ? ? > _ ? ? ? ? ? ? ? ? ? ? ? # = ! ) ? ? ? ? ? } ? ? ? ? ? ? ? ? > ? + ? ? ? ? ? ? ' ? ? ? / ? ? ? ? ? ? ? ? ? ? $ ? - ? | ? ? ? ? = ? ? ? ? ? ? ? ? ? % [ ? ? ? ? ? ? ? < ? ? > ? ? ? : ? ] < ? ? ? ? ? ? ? ? | ? < ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ) ? ? - ? ? ? ) ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? * ? ? ? > ? ? ? ? ? ? ? / { ? ? ? ? @ ? ? ? ? ? ? ? ? ? ? $ ? \u007f / | ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ~ ? ? ? ? ? ? / ? ? \u007f ' ? ? ? ? ? ? ? ? ? ? ? ? ? > ? ? ? ? ? ? ? ? ? ? ? & ? ? ? ? ? ? ; ? ? ? & ? ? ? ? ? ? ? ? ~ ? ? ? ? ? ? \" \" ? ? ? ? ? ? ? ? ? ? ? ? . & ? ? ? ? ? ? ? ? ~ ? & ? ? ? ? ? ? _ ? _ ? ? ? ? ? ? ? ? % ? ? ? ? ? ? ? ? ? # ? } ? ? ? ? ^ ? = ? } ? ? ? ? ? & ? . > ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? * ? ' ? < ? ? ? ? ? | \\ ? ? ? ? ? / ? ? $ # ? ? ? ? ? / ? ? = ? + ? ? ? ? ? ? ? \u007f [ ? ? ? ~ ? ? ? ? ? ? * ? ? ? ? ? ? ? ? ? ? ? _ ? ? * ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? \\ ? ? ? ? ? ? ? ( ? ? ? ? ? ? ? ? ? ) ` : . ? ? ? # ? ? ? ? ? ? ? ? ` ? ? ? ? ' ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? / > ? ? ? ? ? ? ? ? ! ? ? ? ? ? ? ? ? ? ? ? ? ? $ ? ? & > ? ? % _ / ? - ? ? ? ? ? ? ) \u0080 ? # ? ? ? ? ? ? ? % ? ? ? ? \u007f ? ` { ? ? ? ? ? * ? \u007f ? ? ? ? ? ? ? ? ? ? \u007f ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? \"")

    cvt_fn = FUSpWC(arg_list=[200, 255], stat_dict=dict())

    for str_data in str_data_list:
        print(cvt_fn.apply(str_data))
        print("".join(cvt_fn.remove_common_word(str_data)))
