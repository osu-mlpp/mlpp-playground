#!/bin/bash
# Change the utf8mb4_0900_ai_ci COLLATE in sql files to utf8mb4_general_ci, to make it compatible with MariaDB

sed -i -e 's/utf8mb4_0900_ai_ci/utf8mb4_general_ci/g' **/*.sql