# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""WMT19: Translate dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import wmt

_URL = "http://www.statmt.org/wmt18/translation-task.html"
_CITATION = ""

_LANGUAGE_PAIRS = [
    (lang, "en") for lang in ["cs", "de", "et", "fi", "kk", "ru", "tr", "zh"]
]


class Wmt18Translate(wmt.WmtTranslate):
  """WMT 18 translation datasets for all language pairs."""

  BUILDER_CONFIGS = [
      wmt.WmtConfig(  # pylint:disable=g-complex-comprehension
          description="WMT 2018 translation task dataset.",
          url=_URL,
          citation=_CITATION,
          language_pair=(l1, l2),
          version="0.0.1")
      for l1, l2 in _LANGUAGE_PAIRS
  ]

  @property
  def _subsets(self):
    return {
        tfds.Split.TRAIN: [
            "europarl_v7", "europarl_v8", "paracrawl_v1", "commoncrawl",
            "newscommentary_v13", "czeng_17", "yandexcorpus",
            "wikiheadlines_fi", "wikiheadlines_ru", "setimes_2",
            "uncorpus_v1_ru", "uncorpus_v1_zh", "rapid_2016"
        ] + wmt.CWMT_SUBSET_NAMES,
        tfds.Split.VALIDATION: [
            "newsdev2014", "newsdev2015", "newsdev2016", "newsdev2017",
            "newsdev2018", "newsdiscussdev2015", "newsdiscusstest2015",
            "newssyscomb2009", "newstest2008", "newstest2009", "newstest2010",
            "newstest2011", "newstest2012", "newstest2013", "newstest2014",
            "newstest2015", "newstest2016", "newstestB2016", "newstest2017",
            "newstestB2017"],
        tfds.Split.TEST: [
            "newstest2018"
        ]
    }
