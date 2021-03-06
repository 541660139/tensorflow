# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Tests for `tf.data.Dataset.filter_with_legacy_function()`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.data.kernel_tests import filter_test_base
from tensorflow.python.framework import test_util
from tensorflow.python.platform import test


@test_util.run_v1_only
class FilterWithLegacyFunctionTest(filter_test_base.FilterTestBase):

  def apply_filter(self, input_dataset, predicate):
    return input_dataset.filter_with_legacy_function(predicate)


if __name__ == "__main__":
  test.main()
