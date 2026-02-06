/*
 * SPDX-License-Identifier: GPL-2.0-only
 *
 * Copyright (C) 2026 Thomas Heijligen <thomas.heijligen@stud.tu-darmstadt.de>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation.
 */

/*
 * This program generates matrices to test the HDTV MatOp Transpose function.
 *
 * First build src/hdtv/rootext/mfile-root/mfile and copy the libmfile.so and
 * mfile.h into this directory. To compile this file, run
 *
 *   cc -o create_mtx create_mtx.c -Wl,-rpath,'$ORIGIN' -I. -L. -lmfile
 *
 * To create a matrix and it's transpose, run
 *
 *   ./create_mtx <simple|complex> <lines> <columns>
 *
 * E.g. `./create_mtx simple 600 800` creates a 'simple.mtx' with 600 lines and
 * 800 columns, and a transposed 'simple.tmtx' with 800 lines and 600 columns.
 *
 * The `simple` mode produces a matrix with it's 1st column set to 600 and a
 * transposed matrix with it's 1st line set to 600.
 *
 * 0-------    0-----
 * |6 0 0 0    |6 6 6
 * |6 0 0 0 => |0 0 0
 * |6 0 0 0    |0 0 0
 *             |0 0 0
 *
 * The `complex` mode produces a matrix where every value is unique. Since the
 * default format is MAT_LC (line compressed), the resulting matrices are quite
 * large.
 *
 * 0-------    0-----
 * |0 1 2 3    |0 4 8
 * |4 5 6 7 => |1 5 9
 * |8 9 A B    |2 6 A
 *             |3 7 B
 *
 */

#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "mfile.h"

static MFILE *mcreate(const char *name, unsigned lines, unsigned columns) {
  MFILE *mtx = mopen(name, "w");
  if (!mtx) {
    return NULL;
  }

  minfo info;
  if (mgetinfo(mtx, &info)) {
    mclose(mtx);
    return NULL;
  }

  info.levels = 1;
  info.lines = lines;
  info.columns = columns;

  if (msetinfo(mtx, &info)) {
    mclose(mtx);
    return NULL;
  }

  return mtx;
}

static int simple(unsigned lines, unsigned columns) {
  const char *MTX_NAME = "simple.mtx";
  const char *TMTX_NAME = "simple.tmtx";
  const double VALUE = 600;
  MFILE *mtx;
  double *buffer;

  mtx = mcreate(MTX_NAME, lines, columns);
  if (!mtx) {
    printf("Failed to create '%s'\n", MTX_NAME);
    return -1;
  }

  buffer = calloc(columns, sizeof(*buffer));
  if (!buffer) {
    mclose(mtx);
    printf("Failed to create buffer of size %u\n", columns);
    return -1;
  }
  buffer[0] = VALUE;

  for (unsigned l = 0; l < lines; l++) {
    if (mputdbl(mtx, buffer, 0, (int32_t)l, 0, (int32_t)columns) != (int32_t)columns) {
      free(buffer);
      mclose(mtx);
      printf("Failed to write '%s' line %u\n", MTX_NAME, l);
      return -1;
    }
  }
  free(buffer);
  mclose(mtx);

  mtx = mcreate(TMTX_NAME, columns, lines);
  if (!mtx) {
    printf("Failed to create '%s'\n", TMTX_NAME);
    return -1;
  }

  buffer = calloc(lines, sizeof(*buffer));
  if (!buffer) {
    mclose(mtx);
    printf("Failed to create buffer of size %u\n", columns);
    return -1;
  }
  for (unsigned i = 0; i < lines; i++) {
    buffer[i] = VALUE;
  }

  if (mputdbl(mtx, buffer, 0, 0, 0, (int32_t)lines) != (int32_t)lines) {
    free(buffer);
    mclose(mtx);
    printf("Failed to write '%s' line 0\n", TMTX_NAME);
    return -1;
  }

  for (unsigned i = 0; i < lines; i++) {
    buffer[i] = 0;
  }

  for (unsigned c = 1; c < columns; c++) {
    if (mputdbl(mtx, buffer, 0, (int32_t)c, 0, (int32_t)lines) != (int32_t)lines) {
      free(buffer);
      mclose(mtx);
      printf("Failed to write '%s' line %u\n", TMTX_NAME, c);
      return -1;
    }
  }
  free(buffer);
  mclose(mtx);

  return 0;
}

static int complex(unsigned lines, unsigned columns) {
  const char *MTX_NAME = "complex.mtx";
  const char *TMTX_NAME = "complex.tmtx";
  MFILE *mtx;
  double *buffer;

  mtx = mcreate(MTX_NAME, lines, columns);
  if (!mtx) {
    printf("Failed to create '%s'\n", MTX_NAME);
    return -1;
  }

  buffer = calloc(columns, sizeof(*buffer));
  if (!buffer) {
    mclose(mtx);
    printf("Failed to create buffer of size %u\n", columns);
    return -1;
  }

  for (unsigned l = 0; l < lines; l++) {
    for (unsigned c = 0; c < columns; c++) {
      buffer[c] = (l * lines) + c;
    }
    if (mputdbl(mtx, buffer, 0, (int32_t)l, 0, (int32_t)columns) != (int32_t)columns) {
      free(buffer);
      mclose(mtx);
      printf("Failed to write '%s' line %u\n", MTX_NAME, l);
      return -1;
    }
  }

  free(buffer);
  mclose(mtx);

  mtx = mcreate(TMTX_NAME, columns, lines);
  if (!mtx) {
    printf("Failed to create '%s'\n", TMTX_NAME);
    return -1;
  }

  buffer = calloc(lines, sizeof(*buffer));
  if (!buffer) {
    mclose(mtx);
    printf("Failed to create buffer of size %u\n", lines);
    return -1;
  }

  for (unsigned c = 0; c < columns; c++) {
    for (unsigned l = 0; l < lines; l++) {
      buffer[l] = (l * lines) + c;
    }
    if (mputdbl(mtx, buffer, 0, (int32_t)c, 0, (int32_t)lines) != (int32_t)lines) {
      free(buffer);
      mclose(mtx);
      printf("Failed to write '%s' line %u\n", MTX_NAME, c);
      return -1;
    }
  }

  free(buffer);
  mclose(mtx);

  return 0;
}

static void print_help(const char *argv0) {
  printf("Usage %s <simple|complex> <lines> <columns>\n\n"
         "  e.g. '%s simple 600 800` creates a 'simple.mtx' with 600 lines and 800"
         "  columns, and a transposed 'simple.tmtx' with 800 lines and 600 columns",
         argv0, argv0);
}

int main(int argc, char *argv[]) {
  if (argc != 4) {
    print_help(argv[0]);
    return -1;
  }

  errno = 0;
  const unsigned lines = (unsigned)strtoul(argv[2], NULL, 10);
  if (errno == ERANGE) {
    printf("Failed to parse <lines>\n\n");
    print_help(argv[0]);
    return -1;
  }
  const unsigned columns = (unsigned)strtoul(argv[3], NULL, 10);
  if (errno == ERANGE) {
    printf("Failed to parse <columns>\n\n");
    print_help(argv[0]);
    return -1;
  }

  if (!strcmp(argv[1], "simple")) {
    return simple(lines, columns);
  }

  if (!strcmp(argv[1], "complex")) {
    return complex(lines, columns);
  }

  print_help(argv[0]);
  return -1;
}
