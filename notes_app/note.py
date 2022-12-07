# Unless explicitly stated otherwise all files in this repository are dual-licensed
# under the Apache 2.0 or BSD3 Licenses.
#
# This product includes software developed at Datadog (https://www.datadoghq.com/)
# Copyright 2022 Datadog, Inc.
class Note:

    def __init__(self, description, id):
        self.id = id
        self.description = description

    def __str__(self):
        return "(" + str(self.id) + ", " + self.description + ")"
