#include <Python.h>

void print_list_info(PyObject* list) {
    Py_ssize_t size = PyList_Size(list);
    printf("List size: %zd\n", size);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject* item = PyList_GetItem(list, i);
        if (item != NULL) {
            PyObject_Print(item, stdout, Py_PRINT_RAW);
            printf("\n");
        }
    }
}

void print_bytes_info(PyObject* bytes) {
    Py_ssize_t size = PyBytes_Size(bytes);
    printf("Bytes size: %zd\n", size);

    const char* data = PyBytes_AsString(bytes);
    if (data != NULL) {
        printf("Bytes data: ");
        for (Py_ssize_t i = 0; i < size; i++) {
            printf("%02x ", (unsigned char)data[i]);
        }
        printf("\n");
    }
}
