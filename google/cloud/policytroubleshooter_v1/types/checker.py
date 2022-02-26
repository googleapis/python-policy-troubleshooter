# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
import proto  # type: ignore

from google.cloud.policytroubleshooter_v1.types import explanations


__protobuf__ = proto.module(
    package="google.cloud.policytroubleshooter.v1",
    manifest={"TroubleshootIamPolicyRequest", "TroubleshootIamPolicyResponse",},
)


class TroubleshootIamPolicyRequest(proto.Message):
    r"""Request for
    [TroubleshootIamPolicy][google.cloud.policytroubleshooter.v1.IamChecker.TroubleshootIamPolicy].

    Attributes:
        access_tuple (google.cloud.policytroubleshooter_v1.types.AccessTuple):
            The information to use for checking whether a
            member has a permission for a resource.
    """

    access_tuple = proto.Field(
        proto.MESSAGE, number=1, message=explanations.AccessTuple,
    )


class TroubleshootIamPolicyResponse(proto.Message):
    r"""Response for
    [TroubleshootIamPolicy][google.cloud.policytroubleshooter.v1.IamChecker.TroubleshootIamPolicy].

    Attributes:
        access (google.cloud.policytroubleshooter_v1.types.AccessState):
            Indicates whether the member has the
            specified permission for the specified resource,
            based on evaluating all of the applicable IAM
            policies.
        explained_policies (Sequence[google.cloud.policytroubleshooter_v1.types.ExplainedPolicy]):
            List of IAM policies that were evaluated to
            check the member's permissions, with annotations
            to indicate how each policy contributed to the
            final result.

            The list of policies can include the policy for
            the resource itself. It can also include
            policies that are inherited from higher levels
            of the resource hierarchy, including the
            organization, the folder, and the project.
            To learn more about the resource hierarchy, see
            https://cloud.google.com/iam/help/resource-hierarchy.
    """

    access = proto.Field(proto.ENUM, number=1, enum=explanations.AccessState,)
    explained_policies = proto.RepeatedField(
        proto.MESSAGE, number=2, message=explanations.ExplainedPolicy,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
